"""
Build the denuncia evidence repository.

Para cada una de las 12 mesas Nivel 1 (escaneadas con PDF post-upload)
y 349 mesas Nivel 2 (digitales con firmas humanas post-upload):
  - Copia el PDF original (byte-a-byte) con SHA-256
  - Captura la respuesta API ONPE actual (por si la cambian mañana)
  - Extrae la metadata interna del PDF
  - Para Nivel 2, extrae certificados X.509 y timestamps de cada firma
  - Genera analysis.md human-readable

Al final, escribe manifest.json con SHA-256 de cada artefacto
(tamper-evident: cualquier cambio se detecta).
"""
from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import re
import shutil
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path("C:/Users/itama/openelectionsperu")
DENUNCIA = Path("C:/Users/itama/denuncia")
sys.path.insert(0, str(REPO))

import fitz
from cryptography.hazmat.primitives.serialization import pkcs7
from pipeline.conteo_onpe import ONPEScraper

logging.basicConfig(level=logging.WARNING)


def parse_pdf_date(s):
    if not s:
        return None
    s = s.strip()
    if s.startswith("D:"):
        s = s[2:]
    try:
        if "+" in s or "-" in s[8:]:
            tz_start = max(s.rfind("+"), s.rfind("-", 8))
            dt_part = s[:tz_start]
            tz_part = s[tz_start:].replace("'", "")
            if len(tz_part) == 3:
                tz_part += "00"
            return datetime.strptime(dt_part + tz_part, "%Y%m%d%H%M%S%z").astimezone(timezone.utc)
        return datetime.strptime(s[:14], "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except Exception:
        return None


def find_sig_blocks(raw):
    blocks = []
    for m in re.finditer(rb"/Type\s*/Sig\b", raw):
        i = m.start()
        depth = 0
        start = None
        while i > 0:
            if raw[i:i+2] == b">>":
                depth += 1
            elif raw[i:i+2] == b"<<":
                if depth == 0:
                    start = i
                    break
                depth -= 1
            i -= 1
        if start is None:
            continue
        j = start + 2
        depth = 1
        while j < len(raw) - 1:
            if raw[j:j+2] == b"<<":
                depth += 1
                j += 2
            elif raw[j:j+2] == b">>":
                depth -= 1
                if depth == 0:
                    blocks.append(raw[start:j+2])
                    break
                j += 2
            else:
                j += 1
    return blocks


def extract_signatures(raw):
    """Return list of dicts with name, reason, signing time, certificate subjects."""
    out = []
    for blk in find_sig_blocks(raw):
        sm = re.search(rb"/M\s*\(D:(\d{14})([+-Z][\d\x27]*)?\)", blk)
        m_time = None
        if sm:
            full = b"D:" + sm.group(1) + (sm.group(2) or b"")
            m_time = parse_pdf_date(full.decode("latin-1"))

        rm = re.search(rb"/Reason\s*\(([^\)]*)\)", blk)
        reason = rm.group(1).decode("latin-1", "replace") if rm else ""

        nm = re.search(rb"/Name\s*\(([^\)]*)\)", blk)
        name = nm.group(1).decode("latin-1", "replace") if nm else ""

        cm = re.search(rb"/Contents\s*<([0-9a-fA-F\s]+)>", blk)
        certs = []
        if cm:
            try:
                hex_str = cm.group(1).replace(b" ", b"").replace(b"\n", b"").replace(b"\r", b"")
                hex_str_s = hex_str.decode().rstrip("0")
                if len(hex_str_s) % 2:
                    hex_str_s += "0"
                pkcs7_bytes = bytes.fromhex(hex_str_s)
                for c in pkcs7.load_der_pkcs7_certificates(pkcs7_bytes):
                    certs.append({
                        "subject": c.subject.rfc4514_string(),
                        "issuer": c.issuer.rfc4514_string(),
                        "serial_hex": hex(c.serial_number),
                        "not_before": c.not_valid_before_utc.isoformat() if hasattr(c, "not_valid_before_utc") else c.not_valid_before.isoformat(),
                        "not_after": c.not_valid_after_utc.isoformat() if hasattr(c, "not_valid_after_utc") else c.not_valid_after.isoformat(),
                    })
            except Exception as e:
                certs = [{"error": str(e)[:200]}]

        is_agent = "agente automatizado" in reason.lower() or name == ""

        # Try to extract DNI from name (8 digits in the name string)
        dni = None
        dm = re.search(r"\b(\d{8})\b", name)
        if dm:
            dni = dm.group(1)

        out.append({
            "name": name,
            "dni": dni,
            "reason": reason,
            "signing_time_utc": m_time.isoformat() if m_time else None,
            "is_agent_automatizado": is_agent,
            "certs": certs,
        })
    return out


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


# ─── Load source data ───────────────────────────────────────────────

def load_sources():
    print("Cargando fuentes...")
    ultron_meta = json.loads((REPO / "ultron/store/data/ultron_metadata.json").read_text(encoding="utf-8"))
    firmas_report = json.loads((REPO / "ultron/store/data/ultron_firmas_post_upload.json").read_text(encoding="utf-8"))
    geo = json.loads((REPO / "onpe_mesas_geo.json").read_text(encoding="utf-8"))
    geo_idx = {m["codigo_mesa"]: m for m in geo}

    return ultron_meta, firmas_report, geo_idx


# ─── Per-mesa builder ───────────────────────────────────────────────

async def build_mesa(scraper, codigo_mesa, level, ultron_record, geo_record, out_dir):
    mesa_dir = out_dir / codigo_mesa
    mesa_dir.mkdir(parents=True, exist_ok=True)

    artifacts = {}

    # 1) Copiar PDF original byte-a-byte
    src_pdf = Path(ultron_record["pdf_path"])
    dst_pdf = mesa_dir / "acta.pdf"
    if not src_pdf.exists():
        return {"codigo_mesa": codigo_mesa, "error": f"source PDF not found: {src_pdf}"}
    shutil.copyfile(src_pdf, dst_pdf)
    pdf_sha = sha256_file(dst_pdf)
    artifacts["acta.pdf"] = {"sha256": pdf_sha, "size": dst_pdf.stat().st_size}

    # 2) Capturar API ONPE AHORA (anti-tamper: por si cambian la respuesta)
    api_raw = None
    api_capture_at = datetime.now(timezone.utc).isoformat()
    try:
        api_raw = await scraper.fetch_acta_api(codigo_mesa)
    except Exception as e:
        api_raw = {"error_capture": str(e)}
    api_envelope = {
        "captured_at_utc": api_capture_at,
        "endpoint": f"https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa={codigo_mesa}&idEleccion=10",
        "raw_response": api_raw,
    }
    api_path = mesa_dir / "api_response.json"
    api_text = json.dumps(api_envelope, ensure_ascii=False, indent=2)
    api_path.write_text(api_text, encoding="utf-8")
    artifacts["api_response.json"] = {"sha256": sha256_bytes(api_text.encode("utf-8")), "size": len(api_text.encode("utf-8"))}

    # Extraer datos de votos del API
    api_data = {}
    if api_raw and isinstance(api_raw, dict):
        payload = api_raw.get("payload", {})
        data = payload.get("data") or []
        if data:
            api_data = data[0]

    # 3) Re-leer metadata interna del PDF
    pdf_internal = {}
    try:
        doc = fitz.open(str(dst_pdf))
        pdf_internal = {
            "creation_date_raw": (doc.metadata or {}).get("creationDate"),
            "mod_date_raw": (doc.metadata or {}).get("modDate"),
            "producer": (doc.metadata or {}).get("producer"),
            "creator": (doc.metadata or {}).get("creator"),
            "format": (doc.metadata or {}).get("format"),
            "encrypted": doc.is_encrypted,
            "num_pages": len(doc),
        }
        doc.close()
    except Exception as e:
        pdf_internal = {"error": str(e)}

    pdf_created_dt = parse_pdf_date(pdf_internal.get("creation_date_raw"))
    onpe_uploaded = ultron_record.get("onpe_uploaded_utc")
    onpe_dt = datetime.fromisoformat(onpe_uploaded.replace("Z", "+00:00")) if onpe_uploaded else None
    delta_s = ultron_record.get("delta_create_upload_seconds")

    # 4) Firmas (solo digitales tienen firmas digitales internas)
    sigs = []
    if level == "nivel_2":
        try:
            raw = dst_pdf.read_bytes()
            sigs = extract_signatures(raw)
        except Exception as e:
            sigs = [{"error": str(e)}]
        sig_text = json.dumps({"signatures": sigs}, ensure_ascii=False, indent=2, default=str)
        (mesa_dir / "signatures.json").write_text(sig_text, encoding="utf-8")
        artifacts["signatures.json"] = {"sha256": sha256_bytes(sig_text.encode("utf-8")), "size": len(sig_text.encode("utf-8"))}

    # 5) Metadata consolidada
    meta = {
        "codigo_mesa": codigo_mesa,
        "level": level,
        "captured_at_utc": api_capture_at,
        "ubicacion": {
            "departamento": geo_record.get("departamento"),
            "provincia": geo_record.get("provincia"),
            "distrito": geo_record.get("distrito"),
            "ubigeo": geo_record.get("ubigeo"),
            "codigo_estado_acta_indice": geo_record.get("codigo_estado_acta"),
        },
        "votos_api_onpe": {
            "estado_acta": api_data.get("descripcionEstadoActa"),
            "codigo_estado_acta": api_data.get("codigoEstadoActa"),
            "local_votacion": api_data.get("nombreLocalVotacion"),
            "codigo_local": api_data.get("codigoLocalVotacion"),
            "total_electores_habiles": api_data.get("totalElectoresHabiles"),
            "total_votos_emitidos": api_data.get("totalVotosEmitidos"),
            "total_votos_validos": api_data.get("totalVotosValidos"),
            "porcentaje_participacion": api_data.get("porcentajeParticipacionCiudadana"),
        },
        "pdf_internal": pdf_internal,
        "pdf_sha256": pdf_sha,
        "pdf_size_bytes": dst_pdf.stat().st_size,
        "timestamps": {
            "onpe_uploaded_utc": onpe_uploaded,
            "pdf_created_utc": pdf_created_dt.isoformat() if pdf_created_dt else None,
            "delta_create_upload_seconds": delta_s,
            "delta_create_upload_hours": delta_s / 3600 if delta_s is not None else None,
            "delta_create_upload_days": delta_s / 86400 if delta_s is not None else None,
        },
        "n_firmas_digitales": len(sigs),
    }
    if level == "nivel_2" and sigs:
        humans = [s for s in sigs if not s.get("is_agent_automatizado")]
        agents = [s for s in sigs if s.get("is_agent_automatizado")]
        def hd(iso):
            if not iso or not onpe_dt:
                return None
            try:
                return (datetime.fromisoformat(iso.replace("Z", "+00:00")) - onpe_dt).total_seconds() / 3600
            except Exception:
                return None
        meta["firmas_summary"] = {
            "n_humanos": len(humans),
            "n_agentes": len(agents),
            "primer_humano_utc": humans[0]["signing_time_utc"] if humans else None,
            "ultimo_humano_utc": humans[-1]["signing_time_utc"] if humans else None,
            "delta_primer_humano_h": hd(humans[0]["signing_time_utc"]) if humans else None,
            "delta_ultimo_humano_h": hd(humans[-1]["signing_time_utc"]) if humans else None,
            "delta_agente_h": hd(agents[0]["signing_time_utc"]) if agents else None,
            "humanos_post_upload": all(hd(h["signing_time_utc"]) > 0 for h in humans if h.get("signing_time_utc")),
            "humanos": [{"name": h["name"], "dni": h.get("dni"), "signing_time_utc": h["signing_time_utc"]} for h in humans],
        }

    meta_text = json.dumps(meta, ensure_ascii=False, indent=2, default=str)
    (mesa_dir / "metadata.json").write_text(meta_text, encoding="utf-8")
    artifacts["metadata.json"] = {"sha256": sha256_bytes(meta_text.encode("utf-8")), "size": len(meta_text.encode("utf-8"))}

    # 6) analysis.md (human-readable)
    md = render_analysis_md(meta)
    (mesa_dir / "analysis.md").write_text(md, encoding="utf-8")
    artifacts["analysis.md"] = {"sha256": sha256_bytes(md.encode("utf-8")), "size": len(md.encode("utf-8"))}

    return {"codigo_mesa": codigo_mesa, "level": level, "artifacts": artifacts, "meta": meta}


PERU_TZ = timezone(timedelta(hours=-5))


def to_lima(iso):
    """Convierte ISO 8601 UTC a string en hora Lima (UTC-5)."""
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(PERU_TZ)
        return dt.strftime("%Y-%m-%d %H:%M:%S") + " (Lima)"
    except Exception:
        return None


def render_analysis_md(meta):
    cm = meta["codigo_mesa"]
    u = meta["ubicacion"]
    v = meta["votos_api_onpe"]
    t = meta["timestamps"]
    level = meta["level"]
    delta_h = t.get("delta_create_upload_hours") or 0

    lines = [
        f"# Mesa {cm} — evidencia {'Nivel 1 (escaneada)' if level == 'nivel_1' else 'Nivel 2 (digital)'}",
        "",
        f"_Capturado: {meta['captured_at_utc']}_",
        "",
        "## Ubicación",
        f"- **Departamento**: {u.get('departamento')}",
        f"- **Provincia**: {u.get('provincia')}",
        f"- **Distrito**: {u.get('distrito')}",
        f"- **Local de votación**: {v.get('local_votacion')} (código {v.get('codigo_local')})",
        f"- **Ubigeo**: {u.get('ubigeo')}",
        "",
        "## Resultado declarado por ONPE",
        f"- Estado del acta: **{v.get('estado_acta')}** (código `{v.get('codigo_estado_acta')}`)",
        f"- Electores hábiles: {v.get('total_electores_habiles')}",
        f"- Votos emitidos: {v.get('total_votos_emitidos')}",
        f"- Votos válidos: {v.get('total_votos_validos')}",
        f"- Participación: {v.get('porcentaje_participacion')}%",
        "",
        "## Los dos timestamps clave",
        "",
        f"| Evento | UTC | Hora Perú (UTC-5) |",
        f"|---|---|---|",
        f"| ONPE registró el voto (`daudFechaCreacion`) | `{t['onpe_uploaded_utc']}` | `{to_lima(t['onpe_uploaded_utc'])}` |",
        f"| PDF de respaldo creado (`/CreationDate`) | `{t['pdf_created_utc']}` | `{to_lima(t['pdf_created_utc'])}` |",
        "",
        f"**Brecha:** PDF creado **{abs(delta_h):.2f} horas {'DESPUÉS' if delta_h < 0 else 'antes'} del upload** ({abs(delta_h)/24:.2f} días).",
        "",
        "## Verificación independiente",
        "",
        f"1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **{cm}**",
        f"2. Descargar el PDF del acta",
        f"3. Verificar SHA-256: `{meta['pdf_sha256']}`",
    ]

    if level == "nivel_2" and meta.get("firmas_summary"):
        fs = meta["firmas_summary"]
        lines += [
            f"4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)",
            f"5. Click en el icono de pluma (panel \"Firmas\") en la barra izquierda",
            f"6. Verificar las {fs['n_humanos'] + fs['n_agentes']} firmas: **{fs['n_humanos']}** humanas + **{fs['n_agentes']}** \"AGENTE AUTOMATIZADO STAE\"",
            "",
            "## Firmas extraídas del PDF",
            "",
            f"| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |",
            f"|---|---|---|---|---|---|",
        ]
        # Agente row: usar el timestamp del agente, no del primer humano
        agent_iso = meta.get("firmas_summary", {}).get("agent_first_utc") if False else None
        # build_mesa stores agent_first as `agent_first_iso` in metadata; firmas_summary doesn't have it
        # Re-derivamos del campo si existe
        agent_iso = None
        # Fallback: el agente firma siempre antes del upload, calculamos desde delta_agente_h
        if fs.get("delta_agente_h") is not None and meta["timestamps"]["onpe_uploaded_utc"]:
            onpe_dt = datetime.fromisoformat(meta["timestamps"]["onpe_uploaded_utc"].replace("Z", "+00:00"))
            agent_dt = onpe_dt + timedelta(hours=fs["delta_agente_h"])
            agent_iso = agent_dt.isoformat()
        if agent_iso:
            lines.append(
                f"| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `{agent_iso}` | `{to_lima(agent_iso)}` | {fs['delta_agente_h']:+.2f}h |"
            )
        for i, h in enumerate(fs.get("humanos", []), 1):
            iso = h.get("signing_time_utc")
            if iso and meta['timestamps']['onpe_uploaded_utc']:
                onpe_dt = datetime.fromisoformat(meta['timestamps']['onpe_uploaded_utc'].replace('Z', '+00:00'))
                hd = (datetime.fromisoformat(iso.replace('Z', '+00:00')) - onpe_dt).total_seconds() / 3600
                lines.append(f"| {i} | {h['name']} | {h.get('dni') or '?'} | `{iso}` | `{to_lima(iso)}` | {hd:+.2f}h |")
        lines += [
            "",
            f"- **¿Humanos firmaron post-upload?** {'**SÍ**' if fs['humanos_post_upload'] else 'No'}",
            f"- **Primer humano firmó**: {fs['delta_primer_humano_h']:+.2f}h vs upload" if fs.get('delta_primer_humano_h') is not None else "",
            f"- **Último humano firmó**: {fs['delta_ultimo_humano_h']:+.2f}h vs upload" if fs.get('delta_ultimo_humano_h') is not None else "",
        ]
    else:
        lines += [
            f"4. Click derecho sobre el PDF → Propiedades → comparar fecha de creación con `daudFechaCreacion` de la API",
        ]

    return "\n".join(line for line in lines if line is not None) + "\n"


# ─── Manifest ──────────────────────────────────────────────────────

def build_manifest(results):
    """Produce a tamper-evident manifest of all artifacts."""
    files = {}
    for r in results:
        if "error" in r:
            continue
        for fname, info in r["artifacts"].items():
            rel_path = f"{r['level']}_{'escaneadas' if r['level']=='nivel_1' else 'digitales'}/{r['codigo_mesa']}/{fname}"
            files[rel_path] = info
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "n_files": len(files),
        "files": files,
    }


# ─── Main ──────────────────────────────────────────────────────────

async def main():
    ultron_meta, firmas_report, geo_idx = load_sources()

    # Nivel 1: 12 escaneadas con delta negativo
    nivel_1 = [r for r in ultron_meta["resultados"]
               if r.get("tipo_acta") == "escaneada" and not r.get("error")
               and r.get("delta_create_upload_seconds") is not None
               and r["delta_create_upload_seconds"] < 0]
    print(f"Nivel 1 (escaneadas con PDF post-upload): {len(nivel_1)} mesas")

    # Nivel 2: 349 digitales con firmas humanas post-upload
    nivel_2_mesas = {m["codigo_mesa"] for m in firmas_report["mesas"]}
    nivel_2 = [r for r in ultron_meta["resultados"] if r["codigo_mesa"] in nivel_2_mesas]
    print(f"Nivel 2 (digitales con firmas post-upload): {len(nivel_2)} mesas")

    scraper = ONPEScraper()
    results = []
    t0 = time.time()

    for i, rec in enumerate(nivel_1, 1):
        cm = rec["codigo_mesa"]
        print(f"  [N1 {i}/{len(nivel_1)}] {cm}...", end="", flush=True)
        try:
            r = await build_mesa(scraper, cm, "nivel_1", rec, geo_idx.get(cm, {}), DENUNCIA / "nivel_1_escaneadas")
            results.append(r)
            print(" ok")
        except Exception as e:
            print(f" ERROR: {e}")
            results.append({"codigo_mesa": cm, "level": "nivel_1", "error": str(e)})

    for i, rec in enumerate(nivel_2, 1):
        cm = rec["codigo_mesa"]
        print(f"  [N2 {i}/{len(nivel_2)}] {cm}...", end="", flush=True)
        try:
            r = await build_mesa(scraper, cm, "nivel_2", rec, geo_idx.get(cm, {}), DENUNCIA / "nivel_2_digitales")
            results.append(r)
            print(" ok")
        except Exception as e:
            print(f" ERROR: {e}")
            results.append({"codigo_mesa": cm, "level": "nivel_2", "error": str(e)})

    elapsed = time.time() - t0
    print(f"\nProcesado en {elapsed:.0f}s")

    # Manifest — escribir en BINARIO para evitar conversion CRLF en Windows
    manifest = build_manifest(results)
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8")
    (DENUNCIA / "manifest.json").write_bytes(manifest_bytes)
    print(f"manifest.json: {manifest['n_files']} archivos")

    # Hash del manifest (root hash) — también en binario
    root_hash = sha256_bytes(manifest_bytes)
    root_hash_text = (
        f"{root_hash}  manifest.json\n"
        f"# Generado: {datetime.now(timezone.utc).isoformat()}\n"
        f"# Si este hash cambia, el manifest fue modificado.\n"
    )
    (DENUNCIA / "ROOT_HASH.txt").write_bytes(root_hash_text.encode("utf-8"))
    print(f"ROOT_HASH (sha256 del manifest): {root_hash}")

    # CSV index
    rows = ["codigo_mesa,level,departamento,provincia,distrito,onpe_uploaded_utc,pdf_created_utc,delta_horas,votos_validos,pdf_sha256"]
    for r in results:
        if "error" in r:
            continue
        meta = r["meta"]
        u = meta["ubicacion"]
        t = meta["timestamps"]
        v = meta["votos_api_onpe"]
        rows.append(",".join([
            r["codigo_mesa"],
            r["level"],
            u.get("departamento") or "",
            u.get("provincia") or "",
            u.get("distrito") or "",
            t.get("onpe_uploaded_utc") or "",
            t.get("pdf_created_utc") or "",
            f"{(t.get('delta_create_upload_hours') or 0):.2f}",
            str(v.get("total_votos_validos") or ""),
            meta["pdf_sha256"],
        ]))
    (DENUNCIA / "EVIDENCE_INDEX.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("EVIDENCE_INDEX.csv escrito")

    # Resumen
    n1_ok = sum(1 for r in results if r.get("level") == "nivel_1" and "error" not in r)
    n2_ok = sum(1 for r in results if r.get("level") == "nivel_2" and "error" not in r)
    n_errs = sum(1 for r in results if "error" in r)
    print(f"\nResultado: N1 ok={n1_ok}/{len(nivel_1)}, N2 ok={n2_ok}/{len(nivel_2)}, errores={n_errs}")


if __name__ == "__main__":
    asyncio.run(main())
