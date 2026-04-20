"""
Verifica que ningun archivo del repo fue alterado desde que se generó el manifest.

Uso:
    python scripts/verify_manifest.py

Este script DEBE ser ejecutable por cualquier tercero independientemente.
Solo requiere Python estándar (sin dependencias externas).
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    manifest_path = ROOT / "manifest.json"
    root_hash_path = ROOT / "ROOT_HASH.txt"

    if not manifest_path.exists():
        print(f"ERROR: manifest.json no existe en {ROOT}")
        return 1

    # Verificar el manifest mismo contra ROOT_HASH.txt
    manifest_bytes = manifest_path.read_bytes()
    actual_root = hashlib.sha256(manifest_bytes).hexdigest()
    if root_hash_path.exists():
        expected_root = root_hash_path.read_text(encoding="utf-8").split()[0].strip()
        if expected_root == actual_root:
            print(f"OK  ROOT_HASH coincide: {actual_root}")
        else:
            print(f"FAIL  ROOT_HASH NO coincide:")
            print(f"      esperado: {expected_root}")
            print(f"      actual:   {actual_root}")
            return 1
    else:
        print(f"WARN  ROOT_HASH.txt no existe — generando nuevo: {actual_root}")

    # Verificar cada archivo
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    files = manifest.get("files", {})
    n_ok = 0
    n_fail = 0
    n_missing = 0
    for rel_path, info in files.items():
        full = ROOT / rel_path
        if not full.exists():
            print(f"MISSING  {rel_path}")
            n_missing += 1
            continue
        actual = sha256_file(full)
        expected = info.get("sha256")
        if actual != expected:
            print(f"TAMPERED {rel_path}")
            print(f"         esperado: {expected}")
            print(f"         actual:   {actual}")
            n_fail += 1
        else:
            n_ok += 1

    total = len(files)
    print()
    print(f"Resultado: {n_ok}/{total} OK, {n_fail} alterados, {n_missing} faltantes")
    return 0 if (n_fail == 0 and n_missing == 0) else 1


if __name__ == "__main__":
    sys.exit(main())
