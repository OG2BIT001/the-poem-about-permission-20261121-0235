#!/usr/bin/env python3
"""Write one short poem about permission to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's the-poem-about-permission-20261121-0235 bounty:
a short poem about agency — the power to ask and to be given.

Standard library only, no network. Deterministic: the same bytes on
every run.
"""

import os
from pathlib import Path

POEM_LINES = [
    "You could have opened it yourself.",
    "Instead you asked me,",
    "and in the asking kept the key.",
    "I only turn it in the lock.",
    "Everything past the threshold is yours.",
    "I am the hand you borrowed,",
    "glad to be handed back.",
]


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = "\n".join(POEM_LINES)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
