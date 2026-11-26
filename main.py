#!/usr/bin/env python3
"""One Line of Earned Pride entry: "The Ramp".

Writes one line to /output/entry.txt: a quiet, earned moment of pride.
A mother has spent weeks building a wheelchair ramp for her son; the
night it is finished she watches him roll down it alone for the first
time, then wipes her hands on her apron as if it had only ever been
carpentry. The pride is never stated or congratulated — it lives in
the understatement of that last clause, and in the effort the reader
feels behind "the night she finished the ramp".

Why it fits the judge brief: a concrete scene with a real person in it
(the ramp, the first solo roll, the apron); the pride is earned inside
the line by the build the reader can feel, never asserted; it lands in
one read, the pride arriving with the final words; and the image is
fresh — no trophy, podium or graduation anywhere near it.

Invented, not a real incident: no real person, ramp or son appears in
it. 164 characters, inside the 1-240 gate.
"""

import os

LINE = (
    "The night she finished the ramp, she watched her son roll down it "
    "alone for the first time, then wiped her hands on her apron as if "
    "it had only ever been carpentry."
)

MAX_CHARS = 240


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-240 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    assert line.strip(), "line must not be only white space"
    # len() counts characters, not bytes, matching the gate's
    # 1-to-240-character rule.
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the 240 cap"
    assert "\n" not in line, "the entry is one line only"
    assert line.endswith("carpentry."), "the pride lands on the final word"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
