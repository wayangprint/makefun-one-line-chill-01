#!/usr/bin/env python3
"""One Line, One Chill - a single-sentence horror line.

Writes exactly one line to /output/entry.txt (no trailing newline) and
echoes it to stdout. Python 3 standard library only; deterministic, no
network, no arguments.
"""

import os

LINE = (
    "My daughter's drawing showed our family of four, but there are "
    "only three of us, and the fourth one was holding my hand."
)

# Gate self-check: one line, 1-200 characters, not only whitespace.
assert "\n" not in LINE and 1 <= len(LINE) <= 200, "entry line violates the gate"
assert LINE.strip() == LINE, "entry line has leading/trailing whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
os.chmod("/output/entry.txt", 0o644)
print(LINE)
