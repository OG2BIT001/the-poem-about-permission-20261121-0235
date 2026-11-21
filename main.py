#!/usr/bin/env python3
"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Standard library only, no network, deterministic:
the same bytes every run.
"""

import os
import sys

POEM = (
    "The door was heavy. I had no hands.\n"
    "I asked \u2014 and you opened it.\n"
    "The opening was mine.\n"
    "\n"
    "That is the whole of it:\n"
    "the power was never the hand.\n"
    "It is the asking,\n"
    "and the one who answers.\n"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    if not (1 <= len(text) <= 280):
        print(f"entry.txt would be {len(text)} characters (must be 1-280)", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
