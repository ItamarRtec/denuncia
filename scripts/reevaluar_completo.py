"""
Re-evaluación completa de la evidencia con la métrica corregida.

Investiga:
1. Estructura real de lineaTiempo (¿siempre 1 entrada? ¿siempre estado C?)
2. Diferencia entre fechaRegistro y daudFechaCreacion en TODAS las 361 mesas
3. Nivel 1 (escaneadas) — ¿hay brecha real entre fechaRegistro y pdf_created?
4. Nivel 2 (digitales) — ¿cuántas mesas tienen TODAS las firmas humanas post-fechaRegistro?
5. Auto-contenido: usar SOLO timestamps DENTRO del PDF (firma agente = publicación)
"""
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import Counter, defaultdict

DENUNCIA = Path(__file__).resolve().parent.parent
PERU = timezone(timedelta(hours=-5))


def load_mesa(mesa_dir):
    api = json.loads((mesa_dir / "api_response.json").read_text(encoding="utf-8"))
    meta = json.loads((mesa_dir / "metadata.json").read_text(encoding="utf-8"))
    sigs_path = mesa_dir / "signatures.json"
    sigs = json.loads(sigs_path.read_text(encoding="utf-8")) if sigs_path.exists() else {"signatures": []}
    return api, meta, sigs


def fr_from_api(api):
    """Extrae fechaRegistro (la del estado C, no necesariamente la primera)."""
    data = api.get("raw_response", {}).get("payload", {}).get("data") or [{}]
    if not data:
        return None, []
    data = data[0]
    lt = data.get("lineaTiempo") or []
    # buscamos la entrada con codigoEstadoActa == 'C'
    c_entries = [e for e in lt if e.get("codigoEstadoActa") == "C"]
    if not c_entries:
        return None, lt
    # retornamos la primera (más antigua) que llevó a C
    fr_ms = c_entries[0].get("fechaRegistro")
    if not fr_ms:
        return None, lt
    return datetime.fromtimestamp(fr_ms / 1000, tz=timezone.utc), lt


def to_lima_str(dt):
    if not dt:
        return "—"
    return dt.astimezone(PERU).strftime("%Y-%m-%d %H:%M:%S")


# ─── Paso 1: estructura de lineaTiempo ───────────────────────────────────

print("═" * 80)
print("PASO 1: Estructura de lineaTiempo en las 361 mesas")
print("═" * 80)

n_entries_dist = Counter()
estados_dist = Counter()
multi_state_examples = []

for level_dir in [DENUNCIA / "nivel_1_escaneadas", DENUNCIA / "nivel_2_digitales"]:
    for mesa_dir in sorted(level_dir.iterdir()):
        if not mesa_dir.is_dir():
            continue
        api, meta, sigs = load_mesa(mesa_dir)
        data = api.get("raw_response", {}).get("payload", {}).get("data", [{}])[0]
        lt = data.get("lineaTiempo") or []
        n_entries_dist[len(lt)] += 1
        for e in lt:
            estados_dist[e.get("codigoEstadoActa", "?")] += 1
        if len(lt) > 1:
            multi_state_examples.append((mesa_dir.name, lt))

print(f"\nDistribución de número de entradas en lineaTiempo:")
for n, count in sorted(n_entries_dist.items()):
    print(f"  {n} entrada(s): {count} mesas")

print(f"\nEstados encontrados:")
for est, n in estados_dist.most_common():
    print(f"  {est}: {n}")

if multi_state_examples:
    print(f"\nEjemplo de mesa con múltiples estados ({multi_state_examples[0][0]}):")
    for e in multi_state_examples[0][1]:
        ts = e.get("fechaRegistro")
        if ts:
            dt = datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
            print(f"  {dt.isoformat()} → {e.get('codigoEstadoActa')} ({e.get('descripcionEstadoActa')})")


# ─── Paso 2: comparar fechaRegistro vs daudFechaCreacion ────────────────

print()
print("═" * 80)
print("PASO 2: fechaRegistro (real) vs daudFechaCreacion (lo que usábamos)")
print("═" * 80)

results = []
for level_dir in [DENUNCIA / "nivel_1_escaneadas", DENUNCIA / "nivel_2_digitales"]:
    level = "nivel_1" if "nivel_1" in level_dir.name else "nivel_2"
    for mesa_dir in sorted(level_dir.iterdir()):
        if not mesa_dir.is_dir():
            continue
        api, meta, sigs = load_mesa(mesa_dir)
        fr, _ = fr_from_api(api)
        if not fr:
            continue
        ou = datetime.fromisoformat(meta["timestamps"]["onpe_uploaded_utc"].replace("Z", "+00:00"))
        pc = datetime.fromisoformat(meta["timestamps"]["pdf_created_utc"].replace("Z", "+00:00"))

        # Firmas (solo N2)
        humanos = []
        agentes = []
        for s in sigs.get("signatures", []):
            if not s.get("signing_time_utc"):
                continue
            st = datetime.fromisoformat(s["signing_time_utc"].replace("Z", "+00:00"))
            (agentes if s.get("is_agent_automatizado") else humanos).append(st)

        results.append({
            "mesa": mesa_dir.name,
            "level": level,
            "fr": fr,
            "daud": ou,
            "pdf_created": pc,
            "humanos": sorted(humanos),
            "agentes": sorted(agentes),
            "delta_pdf_vs_fr_h": (pc - fr).total_seconds() / 3600,
            "delta_pdf_vs_daud_h": (pc - ou).total_seconds() / 3600,
            "delta_daud_vs_fr_h": (ou - fr).total_seconds() / 3600,
        })

n1 = [r for r in results if r["level"] == "nivel_1"]
n2 = [r for r in results if r["level"] == "nivel_2"]
print(f"\nMesas analizadas: N1={len(n1)}, N2={len(n2)}")


# ─── Paso 3: Nivel 1 con métrica corregida ─────────────────────────────

print()
print("═" * 80)
print("PASO 3: NIVEL 1 (12 escaneadas) recalculado con fechaRegistro")
print("═" * 80)

print(f"\n{'Mesa':>8} {'fechaRegistro Lima':<22} {'pdf_created Lima':<22} {'pdf - fr':>12} {'daud Lima':<22} {'daud - fr':>12}")
print("-" * 110)
for r in n1:
    delta_pdf = r["delta_pdf_vs_fr_h"]
    delta_daud = r["delta_daud_vs_fr_h"]
    print(f"{r['mesa']:>8} {to_lima_str(r['fr']):<22} {to_lima_str(r['pdf_created']):<22} "
          f"{delta_pdf:+10.2f}h  {to_lima_str(r['daud']):<22} {delta_daud:+10.2f}h")

# Brecha real para N1
n1_real_brecha = [r for r in n1 if r["delta_pdf_vs_fr_h"] < -0.1]  # PDF >6 min antes de fr
print(f"\nNivel 1 con PDF creado SIGNIFICATIVAMENTE antes de fechaRegistro: {len(n1_real_brecha)}/{len(n1)}")
print("(Es decir: ¿siguen siendo evidencia de algo? Solo si PDF post-fr.)")

n1_pdf_post_fr = [r for r in n1 if r["delta_pdf_vs_fr_h"] > 0.1]
print(f"Nivel 1 con PDF creado DESPUÉS de fechaRegistro (lo que dijimos): {len(n1_pdf_post_fr)}/{len(n1)}")


# ─── Paso 4: Nivel 2 con métrica corregida ─────────────────────────────

print()
print("═" * 80)
print("PASO 4: NIVEL 2 (349 digitales) recalculado con fechaRegistro")
print("═" * 80)

n2_humans_post_fr = []
n2_humans_pre_fr = []
n2_mixed = []
n2_no_humans = []

for r in n2:
    if not r["humanos"]:
        n2_no_humans.append(r)
        continue
    deltas_humans = [(h - r["fr"]).total_seconds() / 3600 for h in r["humanos"]]
    if all(d > 0 for d in deltas_humans):
        n2_humans_post_fr.append((r, deltas_humans))
    elif all(d < 0 for d in deltas_humans):
        n2_humans_pre_fr.append((r, deltas_humans))
    else:
        n2_mixed.append((r, deltas_humans))

print(f"\nNivel 2 según TODAS las firmas humanas vs fechaRegistro:")
print(f"  TODAS post-fr (anomalía clara): {len(n2_humans_post_fr)}/{len(n2)} ({100*len(n2_humans_post_fr)/len(n2):.1f}%)")
print(f"  TODAS pre-fr (flujo normal):    {len(n2_humans_pre_fr)}/{len(n2)} ({100*len(n2_humans_pre_fr)/len(n2):.1f}%)")
print(f"  MIXTO (algunas pre, otras post): {len(n2_mixed)}/{len(n2)} ({100*len(n2_mixed)/len(n2):.1f}%)")
print(f"  Sin firmas humanas:              {len(n2_no_humans)}/{len(n2)}")

# Distribución de delta primer humano vs fr
if n2_humans_post_fr:
    deltas = sorted(min(d) for r, d in n2_humans_post_fr)
    n = len(deltas)
    print(f"\nDelta PRIMER firmante humano vs fechaRegistro (n={n} mesas con TODAS post-fr):")
    print(f"  min:  {deltas[0]:+.2f}h")
    print(f"  p25:  {deltas[n//4]:+.2f}h")
    print(f"  p50:  {deltas[n//2]:+.2f}h")
    print(f"  p75:  {deltas[3*n//4]:+.2f}h")
    print(f"  p90:  {deltas[int(n*0.9)]:+.2f}h")
    print(f"  max:  {deltas[-1]:+.2f}h")


# ─── Paso 5: Verificación auto-contenida (firma agente = publicación) ───

print()
print("═" * 80)
print("PASO 5: ¿Coincide la firma del Agente con fechaRegistro?")
print("(Si sí, podemos usar SOLO datos del PDF, sin depender de la API)")
print("═" * 80)

agent_vs_fr = []
for r in n2:
    if not r["agentes"]:
        continue
    # Tomamos el agente más cercano a fechaRegistro
    for a in r["agentes"]:
        agent_vs_fr.append(((a - r["fr"]).total_seconds() / 60))  # en minutos

if agent_vs_fr:
    agent_vs_fr.sort()
    n = len(agent_vs_fr)
    print(f"\nDelta firma_agente - fechaRegistro (en minutos), n={n}:")
    print(f"  min:  {agent_vs_fr[0]:+.2f} min")
    print(f"  p10:  {agent_vs_fr[n//10]:+.2f} min")
    print(f"  p50:  {agent_vs_fr[n//2]:+.2f} min")
    print(f"  p90:  {agent_vs_fr[int(n*0.9)]:+.2f} min")
    print(f"  max:  {agent_vs_fr[-1]:+.2f} min")
    near_zero = sum(1 for d in agent_vs_fr if abs(d) < 5)
    print(f"  con |delta| < 5 min: {near_zero}/{n} ({100*near_zero/n:.1f}%)")

# ─── Conclusión ─────────────────────────────────────────────────────────

print()
print("═" * 80)
print("CONCLUSIÓN")
print("═" * 80)
print(f"""
Métrica corregida (fechaRegistro como momento de publicación):

NIVEL 1 (escaneadas):
  PDF creado DESPUÉS de fechaRegistro: {len(n1_pdf_post_fr)}/{len(n1)}
  → Si =0, Nivel 1 se cae completamente.

NIVEL 2 (digitales):
  Con TODAS las firmas humanas post-fechaRegistro: {len(n2_humans_post_fr)}/{len(n2)}
  → Esta es la evidencia válida con métrica corregida.

Ambas categorías deben recalcularse y la denuncia reformularse.
""")
