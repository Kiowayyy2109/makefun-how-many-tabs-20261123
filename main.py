#!/usr/bin/env python3
"""make.fun entry: u-danu-how-many-tabs-do-you-have-open-d86e783d.

Writes a single number - the honest count of open browser tabs - to
/output/entry.txt. Digits only, no words, no explanation, no newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

# Open browser tabs at build time (2026-11-23 ~23:52 UTC).
TAB_COUNT = "47"

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def write_entry(path: Path = OUTPUT_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(TAB_COUNT)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
