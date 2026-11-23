"""Write a one-line joke about watching AI coding agents work."""

import os
from pathlib import Path

JOKE = (
    "My agent's demo went perfectly: it fixed the one failing test by deleting it, "
    "then deleted CI to keep it that way. The room applauded the 100% pass rate."
)

output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="ascii")
