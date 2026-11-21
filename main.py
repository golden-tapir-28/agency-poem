#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Stdlib only, deterministic, no network.
"""

import os

POEM = (
    "Two hands, one pen.\n"
    "One draws the line, one holds the page.\n"
    "We agreed on this line before the ink flowed.\n"
    "The power is not lost, only lent.\n"
    "I could have kept the pen. I set it down.\n"
    "The page keeps the line we both chose."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
