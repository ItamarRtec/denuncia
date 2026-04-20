"""
Pide a archive.org (Wayback Machine) que capture snapshots de las páginas
ONPE de las mesas más críticas. Esto crea un testigo independiente externo:
si ONPE modifica los datos después, queda registro inmutable de qué se mostraba.

Uso:
    python scripts/archive_onpe_snapshots.py
"""
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

DENUNCIA = Path(__file__).resolve().parent.parent

# URLs ONPE a archivar por mesa
def urls_for_mesa(codigo_mesa: str) -> list[str]:
    return [
        f"https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa={codigo_mesa}&idEleccion=10",
    ]


def save_to_wayback(url: str, retries: int = 3) -> dict:
    """POST a https://web.archive.org/save/<url> y devuelve la URL del snapshot."""
    save_url = f"https://web.archive.org/save/{url}"
    req = Request(save_url, headers={"User-Agent": "denuncia-evidence/1.0"})
    last_err = None
    for attempt in range(retries):
        try:
            with urlopen(req, timeout=120) as resp:
                snapshot_url = resp.headers.get("content-location") or resp.url
                return {"ok": True, "snapshot_url": snapshot_url, "status": resp.status}
        except HTTPError as e:
            last_err = f"HTTP {e.code}: {e.reason}"
            if e.code in (429, 502, 503):
                time.sleep(5 * (attempt + 1))
                continue
            return {"ok": False, "error": last_err}
        except URLError as e:
            last_err = str(e)
            time.sleep(5 * (attempt + 1))
    return {"ok": False, "error": last_err or "unknown"}


def main():
    out_dir = DENUNCIA / "archive_org_snapshots"
    out_dir.mkdir(exist_ok=True)
    log = []

    # Las 12 Nivel 1 (todas — son las más críticas)
    nivel_1 = sorted(d.name for d in (DENUNCIA / "nivel_1_escaneadas").iterdir() if d.is_dir())

    # Sample 20 random Nivel 2 para tener evidencia distribuida
    import random
    random.seed(42)
    nivel_2 = sorted(d.name for d in (DENUNCIA / "nivel_2_digitales").iterdir() if d.is_dir())
    nivel_2_sample = random.sample(nivel_2, min(20, len(nivel_2)))

    targets = []
    for cm in nivel_1:
        targets.append(("nivel_1", cm))
    for cm in nivel_2_sample:
        targets.append(("nivel_2_sample", cm))

    print(f"Archivando {len(targets)} mesas en archive.org...")
    print("(Wayback Save Page Now puede tomar 1-2 min por URL)")

    for category, cm in targets:
        for url in urls_for_mesa(cm):
            print(f"  [{category}] {cm}  {url}")
            res = save_to_wayback(url)
            entry = {"category": category, "codigo_mesa": cm, "url": url, **res}
            log.append(entry)
            if res.get("ok"):
                print(f"    -> OK: {res.get('snapshot_url')}")
            else:
                print(f"    -> FAIL: {res.get('error')}")
            # Rate limit sano
            time.sleep(3)

    # Guardar log
    log_path = out_dir / "archive_log.json"
    log_path.write_bytes(json.dumps({
        "generated_at_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        "n_targets": len(log),
        "n_ok": sum(1 for e in log if e.get("ok")),
        "n_fail": sum(1 for e in log if not e.get("ok")),
        "entries": log,
    }, ensure_ascii=False, indent=2).encode("utf-8"))
    print(f"\nLog: {log_path}")
    print(f"OK: {sum(1 for e in log if e.get('ok'))}, FAIL: {sum(1 for e in log if not e.get('ok'))}")


if __name__ == "__main__":
    main()
