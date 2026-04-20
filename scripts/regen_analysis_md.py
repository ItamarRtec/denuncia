"""Regenera analysis.md de cada mesa desde metadata.json existente (no re-baja datos)."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_evidence import render_analysis_md  # noqa

DENUNCIA = Path(__file__).resolve().parent.parent

n = 0
for level_dir in [DENUNCIA / "nivel_1_escaneadas", DENUNCIA / "nivel_2_digitales"]:
    for mesa_dir in level_dir.iterdir():
        if not mesa_dir.is_dir():
            continue
        meta_path = mesa_dir / "metadata.json"
        if not meta_path.exists():
            continue
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        md = render_analysis_md(meta)
        (mesa_dir / "analysis.md").write_bytes(md.encode("utf-8"))
        n += 1

print(f"Regenerados {n} analysis.md")
