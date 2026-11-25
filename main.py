#!/usr/bin/env python3
"""One-line review of the most boring object: a doorstop.

Writes the fixed review line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


LINE = (
    "Five stars. It's held the same door open since 2019 without a sick day, "
    "a raise, or one LinkedIn post about the grind."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
