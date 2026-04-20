"""
Análisis de control: ¿en mesas digitales NORMALES (no anómalas), las firmas humanas
ocurren ANTES o DESPUÉS de fechaRegistro?

Sampleamos 100 mesas digitales aleatorias que NO están en nuestras 337 anómalas
ni en las 12 descartadas. Para cada una:
  1. Re-fetch buscar/mesa de la API ONPE → extraer lineaTiempo[i].fechaRegistro estado C
  2. Leemos su PDF (en ultron/store/pdfs/) y extraemos firmas humanas
  3. Computamos delta humanos vs fechaRegistro

Si el patrón normal es "humanos firman ANTES de fechaRegistro", entonces las 337
son outliers genuinos (denuncia fuerte). Si en muchas normales también hay humanos
post-fr, la denuncia se debilita.
"""
import asyncio
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path

REPO = Path("C:/Users/itama/openelectionsperu")
DENUNCIA = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from cryptography.hazmat.primitives.serialization import pkcs7
from pipeline.conteo_onpe import ONPEScraper

PERU = timezone(timedelta(hours=-5))


def parse_pdf_date(s):
    if not s: return None
    s = s.strip()
    if s.startswith("D:"): s = s[2:]
    try:
        if "+" in s or "-" in s[8:]:
            tz_start = max(s.rfind("+"), s.rfind("-", 8))
            dt_part = s[:tz_start]
            tz_part = s[tz_start:].replace("'", "")
            if len(tz_part) == 3: tz_part += "00"
            return datetime.strptime(dt_part + tz_part, "%Y%m%d%H%M%S%z").astimezone(timezone.utc)
        return datetime.strptime(s[:14], "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    except Exception: return None


def find_sig_blocks(raw):
    blocks = []
    for m in re.finditer(rb'/Type\s*/Sig\b', raw):
        i = m.start(); depth = 0; start = None
        while i > 0:
            if raw[i:i+2] == b">>": depth += 1
            elif raw[i:i+2] == b"<<":
                if depth == 0: start = i; break
                depth -= 1
            i -= 1
        if start is None: continue
        j = start + 2; depth = 1
        while j < len(raw) - 1:
            if raw[j:j+2] == b"<<": depth += 1; j += 2
            elif raw[j:j+2] == b">>":
                depth -= 1
                if depth == 0: blocks.append(raw[start:j+2]); break
                j += 2
            else: j += 1
    return blocks


def extract_humans_and_agent(raw):
    """Devuelve (humans, agent) con timestamps UTC."""
    humans, agents = [], []
    for blk in find_sig_blocks(raw):
        sm = re.search(rb"/M\s*\(D:(\d{14})([+-Z][\d\x27]*)?\)", blk)
        if not sm: continue
        full = b"D:" + sm.group(1) + (sm.group(2) or b"")
        t = parse_pdf_date(full.decode("latin-1"))
        if not t: continue
        rm = re.search(rb"/Reason\s*\(([^\)]*)\)", blk)
        reason = rm.group(1).decode("latin-1", "replace") if rm else ""
        nm = re.search(rb"/Name\s*\(([^\)]*)\)", blk)
        name = nm.group(1).decode("latin-1", "replace") if nm else ""
        is_agent = "agente automatizado" in reason.lower() or name == ""
        (agents if is_agent else humans).append(t)
    humans.sort(); agents.sort()
    return humans, agents


async def main():
    import random

    # Excluir las 337 + 12 que ya analizamos
    excluidas = set()
    for d in (DENUNCIA / "mesas_anomalas").iterdir():
        if d.is_dir(): excluidas.add(d.name)
    for d in (DENUNCIA / "mesas_descartadas").iterdir():
        if d.is_dir(): excluidas.add(d.name)
    print(f"Excluidas (ya analizadas): {len(excluidas)}")

    # Universo: digitales OK del ULTRON
    ultron = json.loads((REPO / "ultron/store/data/ultron_metadata.json").read_text(encoding="utf-8"))
    digitales_ok = [r for r in ultron["resultados"]
                    if r.get("tipo_acta") == "digital"
                    and not r.get("error")
                    and r["codigo_mesa"] not in excluidas
                    and r.get("pdf_path") and Path(r["pdf_path"]).exists()]
    print(f"Universo digitales OK no analizadas: {len(digitales_ok)}")

    random.seed(42)
    sample = random.sample(digitales_ok, min(100, len(digitales_ok)))
    print(f"Muestreando {len(sample)} mesas para baseline...")
    print()

    scraper = ONPEScraper()
    results = []
    for i, r in enumerate(sample, 1):
        cm = r["codigo_mesa"]
        try:
            api = await scraper.fetch_acta_api(cm)
            data = (api.get("payload") or {}).get("data") or [{}]
            data = data[0] if data else {}
            lt = data.get("lineaTiempo") or []
            c_entries = [e for e in lt if e.get("codigoEstadoActa") == "C"]
            if not c_entries:
                results.append({"mesa": cm, "error": "sin estado C"})
                continue
            fr = datetime.fromtimestamp(c_entries[0]["fechaRegistro"]/1000, tz=timezone.utc)
            raw = Path(r["pdf_path"]).read_bytes()
            humans, agents = extract_humans_and_agent(raw)
            if not humans:
                results.append({"mesa": cm, "error": "sin firmas humanas"})
                continue
            deltas_h = [(h - fr).total_seconds()/3600 for h in humans]
            delta_a = [(a - fr).total_seconds()/3600 for a in agents] if agents else []
            results.append({
                "mesa": cm,
                "fr_utc": fr.isoformat(),
                "delta_humanos_h": deltas_h,
                "delta_agente_h": delta_a[0] if delta_a else None,
                "todos_humanos_post_fr": all(d > 0.1 for d in deltas_h),
                "todos_humanos_pre_fr": all(d < -0.1 for d in deltas_h),
            })
        except Exception as e:
            results.append({"mesa": cm, "error": str(e)[:60]})
        if i % 20 == 0:
            print(f"  {i}/{len(sample)}...")

    # Análisis
    ok = [r for r in results if "error" not in r]
    err = [r for r in results if "error" in r]
    print(f"\nProcessed: {len(ok)} ok, {len(err)} con error")

    n_post = sum(1 for r in ok if r["todos_humanos_post_fr"])
    n_pre = sum(1 for r in ok if r["todos_humanos_pre_fr"])
    n_mix = sum(1 for r in ok if not r["todos_humanos_post_fr"] and not r["todos_humanos_pre_fr"])

    print()
    print("═" * 60)
    print("BASELINE — mesas digitales NORMALES (no anómalas)")
    print("═" * 60)
    print(f"  TODAS firmas humanas ANTES de fechaRegistro (flujo correcto):  {n_pre}/{len(ok)} ({100*n_pre/len(ok):.1f}%)")
    print(f"  TODAS firmas humanas DESPUÉS de fechaRegistro (anomalía):      {n_post}/{len(ok)} ({100*n_post/len(ok):.1f}%)")
    print(f"  MIXTO (algunas pre, otras post):                               {n_mix}/{len(ok)} ({100*n_mix/len(ok):.1f}%)")

    # Distribución de delta primer humano vs fr
    deltas_first = sorted(r["delta_humanos_h"][0] for r in ok)
    n = len(deltas_first)
    if n:
        print()
        print(f"Delta PRIMER firmante humano vs fechaRegistro (n={n}):")
        for pct in [10, 25, 50, 75, 90]:
            print(f"  p{pct:02d}: {deltas_first[int(n*pct/100)]:+.2f}h")
        print(f"  min: {deltas_first[0]:+.2f}h")
        print(f"  max: {deltas_first[-1]:+.2f}h")

    # Sample some interesting cases
    print()
    print("Sample de los más extremos en cada dirección:")
    sorted_ok = sorted(ok, key=lambda r: r["delta_humanos_h"][0])
    print("  Más NEGATIVOS (humanos firmaron mucho ANTES de fr):")
    for r in sorted_ok[:5]:
        print(f"    {r['mesa']}: {r['delta_humanos_h'][0]:+.2f}h (humano1), agente: {r['delta_agente_h']:+.2f}h" if r['delta_agente_h'] is not None else f"    {r['mesa']}: {r['delta_humanos_h'][0]:+.2f}h")
    print("  Más POSITIVOS (humanos firmaron mucho DESPUÉS de fr):")
    for r in sorted_ok[-5:]:
        print(f"    {r['mesa']}: {r['delta_humanos_h'][0]:+.2f}h (humano1)")

    # Save report
    out = DENUNCIA / "scripts" / "baseline_normales_resultado.json"
    out.write_text(json.dumps({
        "n_sampled": len(sample),
        "n_ok": len(ok),
        "n_humans_pre_fr": n_pre,
        "n_humans_post_fr": n_post,
        "n_mixed": n_mix,
        "delta_first_human_p50_h": deltas_first[len(deltas_first)//2] if deltas_first else None,
        "results": results,
    }, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(f"\nReporte: {out}")


if __name__ == "__main__":
    asyncio.run(main())
