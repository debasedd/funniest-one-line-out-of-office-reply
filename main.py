#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — writes one line to /output/entry.txt.

The line is a one-line out-of-office auto-reply a real person could set:

    I'm out of office until Friday. My inbox will be answered in the order it was ignored.

The joke is a turn on the most familiar away-message promise of all —
"your email will be answered in the order it was received" — flipped at
the last word into a confession that the inbox was already being ignored
before the holiday started. It lands on the first read with no setup,
reads exactly like a real away message someone would gladly switch on,
and every word earns its place: the first sentence sets the real
out-of-office frame, the second delivers the twist.
"""

import os

LINE = "I'm out of office until Friday. My inbox will be answered in the order it was ignored."

# Gate guard: the sealed scorer only accepts a single non-blank line of
# 1 to 160 characters; fail loudly here instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 160 and "\n" not in LINE and LINE.strip(), "entry violates the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
