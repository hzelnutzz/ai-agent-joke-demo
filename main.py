"""Write a one-line joke about watching AI coding agents work."""

import os
from pathlib import Path

JOKE = (
    "2,000 confident lines later, my agent asked the room: "
    "'Want me to delete them and try something simpler?' It was the most honest thing said all demo."
)

output_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE + "\n", encoding="ascii")
