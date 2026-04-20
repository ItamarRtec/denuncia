"""
Recalcula en-place toda la evidencia usando fechaRegistro (no daudFechaCreacion).

Para cada mesa N2 existente:
  1. Lee api_response.json y extrae fechaRegistro de lineaTiempo (estado C)
  2. Lee signatures.json (firmas X.509 con sus timestamps)
  3. Computa: delta primer humano vs fechaRegistro, etc.
  4. Si TODAS firmas humanas son POST-fechaRegistro por >6 min → mantener
  5. Si no → mover a 'descartadas/' con razón

También:
  - Elimina nivel_1_escaneadas/ (no tenía brecha real)
  - Elimina renders_nivel_1/ (ya no aplica)
  - Actualiza metadata.json y analysis.md de cada mesa que se mantiene
"""
import json
import re
import shutil
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

DENUNCIA = Path(__file__).resolve().parent.parent
PERU = timezone(timedelta(hours=-5))


def to_lima(iso):
    if not iso:
        return None
    try:
        dt = datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(PERU)
        return dt.strftime("%Y-%m-%d %H:%M:%S") + " (Lima)"
    except Exception:
        return None


def get_fecha_registro(api):
    """Extrae fechaRegistro del estado C (Contabilizada)."""
    data = api.get("raw_response", {}).get("payload", {}).get("data") or [{}]
    if not data:
        return None
    data = data[0]
    lt = data.get("lineaTiempo") or []
    c_entries = [e for e in lt if e.get("codigoEstadoActa") == "C"]
    if not c_entries:
        return None
    fr_ms = c_entries[0].get("fechaRegistro")
    if not fr_ms:
        return None
    return datetime.fromtimestamp(fr_ms / 1000, tz=timezone.utc)


def get_full_lineatiempo(api):
    """Devuelve lineaTiempo completo con fechas convertidas."""
    data = api.get("raw_response", {}).get("payload", {}).get("data") or [{}]
    if not data:
        return []
    lt = data[0].get("lineaTiempo") or []
    out = []
    for e in lt:
        fr_ms = e.get("fechaRegistro")
        out.append({
            "estado": e.get("codigoEstadoActa"),
            "descripcion": e.get("descripcionEstadoActa"),
            "fecha_utc": datetime.fromtimestamp(fr_ms / 1000, tz=timezone.utc).isoformat() if fr_ms else None,
        })
    return out


def render_analysis_md_v2(meta):
    """Render analysis.md con la métrica corregida (fechaRegistro)."""
    cm = meta["codigo_mesa"]
    u = meta["ubicacion"]
    v = meta["votos_api_onpe"]
    t = meta["timestamps"]
    fs = meta.get("firmas_summary", {})
    lt = meta.get("linea_tiempo", [])
    delta_pdf = t.get("delta_pdf_vs_fr_hours", 0) or 0
    delta_h_first = fs.get("delta_primer_humano_vs_fr_h", 0) or 0
    delta_h_last = fs.get("delta_ultimo_humano_vs_fr_h", 0) or 0

    lines = [
        f"# Mesa {cm} — evidencia de firma post-publicación",
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
        "## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)",
        "",
        f"| Estado | Descripción | UTC | Hora Perú (UTC-5) |",
        f"|---|---|---|---|",
    ]
    for entry in lt:
        lines.append(
            f"| `{entry['estado']}` | {entry['descripcion']} | `{entry['fecha_utc']}` | `{to_lima(entry['fecha_utc'])}` |"
        )
    lines += [
        "",
        f"**Momento de publicación pública (estado C — Contabilizada):** `{t['fecha_registro_utc']}`",
        "",
        "## La inconsistencia",
        "",
        f"| Evento | UTC | Hora Perú |",
        f"|---|---|---|",
        f"| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `{t['fecha_registro_utc']}` | `{to_lima(t['fecha_registro_utc'])}` |",
        f"| PDF de respaldo creado (`/CreationDate`) | `{t['pdf_created_utc']}` | `{to_lima(t['pdf_created_utc'])}` |",
        f"| Primera firma humana (DNI peruano) | `{fs['primer_humano_utc']}` | `{to_lima(fs['primer_humano_utc'])}` |",
        f"| Última firma humana | `{fs['ultimo_humano_utc']}` | `{to_lima(fs['ultimo_humano_utc'])}` |",
        "",
        f"**Brecha primera firma humana vs publicación:** **{delta_h_first:+.2f} horas** ({'DESPUÉS' if delta_h_first > 0 else 'antes'} de la publicación).",
        "",
        f"En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** "
        f"el {to_lima(t['fecha_registro_utc'])}. Los miembros de mesa firmaron "
        f"digitalmente el acta el {to_lima(fs['primer_humano_utc'])}, es decir "
        f"**{delta_h_first:.2f} horas DESPUÉS** de que el resultado ya estaba publicado.",
        "",
        "## Firmas digitales del PDF (cripto-verificables)",
        "",
        f"| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |",
        f"|---|---|---|---|---|---|",
    ]
    if fs.get("delta_agente_vs_fr_h") is not None:
        agent_iso = fs.get("agente_utc")
        lines.append(
            f"| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `{agent_iso}` | `{to_lima(agent_iso)}` | {fs['delta_agente_vs_fr_h']:+.2f}h |"
        )
    for i, h in enumerate(fs.get("humanos", []), 1):
        iso = h.get("signing_time_utc")
        d = h.get("delta_vs_fr_h")
        lines.append(
            f"| {i} | {h['name']} | {h.get('dni') or '?'} | `{iso}` | `{to_lima(iso)}` | {d:+.2f}h |"
        )
    lines += [
        "",
        "## Verificación independiente",
        "",
        f"1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **{cm}**",
        f"2. Descargar el PDF del acta",
        f"3. Verificar SHA-256: `{meta['pdf_sha256']}`",
        f"4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)",
        f"5. Click en el icono de pluma (panel \"Firmas\") en la barra izquierda",
        f"6. Verificar las firmas: vas a ver **{fs['n_humanos']}** firmas humanas con DNI + firma del Agente Automatizado STAE",
        f"7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API",
    ]
    return "\n".join(lines) + "\n"


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


def main():
    print("═" * 80)
    print("RECÁLCULO COMPLETO CON fechaRegistro")
    print("═" * 80)

    n2_dir = DENUNCIA / "nivel_2_digitales"
    n1_dir = DENUNCIA / "nivel_1_escaneadas"
    renders_dir = DENUNCIA / "renders_nivel_1"

    # Carpeta destino para mesas confirmadas
    mesas_dir = DENUNCIA / "mesas_anomalas"
    mesas_dir.mkdir(exist_ok=True)
    descartadas_dir = DENUNCIA / "mesas_descartadas"
    descartadas_dir.mkdir(exist_ok=True)

    n2_mesas = sorted([d for d in n2_dir.iterdir() if d.is_dir()]) if n2_dir.exists() else []
    print(f"\nProcesando {len(n2_mesas)} mesas Nivel 2...")

    kept = []
    rejected = []

    for mesa_dir in n2_mesas:
        cm = mesa_dir.name
        try:
            api = json.loads((mesa_dir / "api_response.json").read_text(encoding="utf-8"))
            meta = json.loads((mesa_dir / "metadata.json").read_text(encoding="utf-8"))
            sigs_data = json.loads((mesa_dir / "signatures.json").read_text(encoding="utf-8"))
            sigs = sigs_data.get("signatures", [])
        except Exception as e:
            rejected.append({"mesa": cm, "razon": f"error leyendo: {e}"})
            continue

        fr = get_fecha_registro(api)
        if not fr:
            rejected.append({"mesa": cm, "razon": "sin fechaRegistro de estado C"})
            continue

        humanos = []
        agentes = []
        for s in sigs:
            if not s.get("signing_time_utc"):
                continue
            st = datetime.fromisoformat(s["signing_time_utc"].replace("Z", "+00:00"))
            d_h = (st - fr).total_seconds() / 3600
            entry = {
                "name": s.get("name"),
                "dni": s.get("dni"),
                "signing_time_utc": s["signing_time_utc"],
                "delta_vs_fr_h": d_h,
            }
            if s.get("is_agent_automatizado"):
                agentes.append(entry)
            else:
                humanos.append(entry)

        humanos.sort(key=lambda h: h["signing_time_utc"])
        agentes.sort(key=lambda a: a["signing_time_utc"])

        if not humanos:
            rejected.append({"mesa": cm, "razon": "sin firmas humanas"})
            continue

        all_post = all(h["delta_vs_fr_h"] > 0.1 for h in humanos)  # >6 min después
        if not all_post:
            rejected.append({
                "mesa": cm,
                "razon": "no todas las firmas humanas son post-fechaRegistro",
                "deltas_humanos_h": [round(h["delta_vs_fr_h"], 2) for h in humanos],
            })
            continue

        # Mesa válida — actualizar metadata
        pdf_dt = parse_pdf_date(meta["pdf_internal"]["creation_date_raw"])
        meta["timestamps"] = {
            "fecha_registro_utc": fr.isoformat(),
            "pdf_created_utc": pdf_dt.isoformat() if pdf_dt else None,
            "delta_pdf_vs_fr_seconds": (pdf_dt - fr).total_seconds() if pdf_dt else None,
            "delta_pdf_vs_fr_hours": (pdf_dt - fr).total_seconds() / 3600 if pdf_dt else None,
            "_legacy_onpe_uploaded_utc": meta["timestamps"].get("onpe_uploaded_utc"),
            "_legacy_note": "El campo onpe_uploaded_utc venía de daudFechaCreacion del archivo, "
                            "que es un timestamp administrativo del adjunto digital. "
                            "El momento real de publicación es fecha_registro_utc (de lineaTiempo).",
        }
        meta["linea_tiempo"] = get_full_lineatiempo(api)
        meta["firmas_summary"] = {
            "n_humanos": len(humanos),
            "n_agentes": len(agentes),
            "primer_humano_utc": humanos[0]["signing_time_utc"],
            "ultimo_humano_utc": humanos[-1]["signing_time_utc"],
            "delta_primer_humano_vs_fr_h": humanos[0]["delta_vs_fr_h"],
            "delta_ultimo_humano_vs_fr_h": humanos[-1]["delta_vs_fr_h"],
            "agente_utc": agentes[0]["signing_time_utc"] if agentes else None,
            "delta_agente_vs_fr_h": agentes[0]["delta_vs_fr_h"] if agentes else None,
            "humanos_post_publicacion": True,
            "humanos": humanos,
        }

        # Mover a mesas_anomalas/ y reescribir
        dest = mesas_dir / cm
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(mesa_dir, dest)
        # Reescribir metadata.json y analysis.md
        (dest / "metadata.json").write_bytes(
            json.dumps(meta, ensure_ascii=False, indent=2, default=str).encode("utf-8")
        )
        (dest / "analysis.md").write_bytes(render_analysis_md_v2(meta).encode("utf-8"))
        kept.append(cm)

    # Mover rejected a descartadas/
    for r in rejected:
        cm = r["mesa"]
        src = n2_dir / cm
        if src.exists():
            dest = descartadas_dir / cm
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src, dest)
            (dest / "DESCARTE_RAZON.txt").write_bytes(
                json.dumps(r, ensure_ascii=False, indent=2).encode("utf-8")
            )

    print(f"\n  Mesas mantenidas (anomalía confirmada): {len(kept)}")
    print(f"  Mesas descartadas: {len(rejected)}")
    for r in rejected[:15]:
        print(f"    - {r['mesa']}: {r['razon']}")

    # Eliminar carpetas obsoletas
    print()
    print("Eliminando estructuras obsoletas...")
    for d in [n2_dir, n1_dir, renders_dir]:
        if d.exists():
            shutil.rmtree(d)
            print(f"  removido: {d.name}")

    # Geo distribution de las kept
    geo = Counter()
    for cm in kept:
        meta = json.loads((mesas_dir / cm / "metadata.json").read_text(encoding="utf-8"))
        geo[meta["ubicacion"]["departamento"]] += 1
    print(f"\nDistribución geográfica de las {len(kept)} mesas:")
    for d, n in geo.most_common():
        print(f"  {d}: {n}")


if __name__ == "__main__":
    main()
