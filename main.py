#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny support line.

A hopeless tech support agent's reply to a desperate customer.
Pure stdlib. Writes the single line to /output/entry.txt and prints it.
"""

import os

LINE = (
    "Have you tried turning it off and on again, or should I just "
    "stay on the line and we can panic together?"
)


def main() -> None:
    # The gate requires 1-199 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 199 and LINE.strip(), "line fails the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
