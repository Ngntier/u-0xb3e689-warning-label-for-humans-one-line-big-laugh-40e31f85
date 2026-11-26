"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for human beings to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Joke angle: the entry plays the label form perfectly straight — a
deadpan "WARNING:" hazard notice for the human "unit" itself, as if
people shipped with the same caution stickers as appliances. The
laugh lands in the last few words: the "hazard" is not an explosion
or a short circuit, but the very human habit of answering "long
story short" with a 45-minute story. Song and tears escalate the
absurdity first, so the story punch feels like the final symptom
on the label, not a separate joke.

Gate rules enforced in validate(): the entry must be a single line
(≤ 160 characters, no newline or control characters), start with
the "WARNING:" label prefix, contain no leading or trailing
whitespace, and be valid UTF-8 text. Output is written byte-for-byte
as the ENTRY constant — no trailing newline is added.
"""

import os
import sys

ENTRY = (
    "WARNING: This unit may spontaneously burst into song, tears, "
    "or a 45-minute story that began with 'long story short.'"
)

MAX_CHARS = 160


def validate(entry: str) -> None:
    """Check the entry against the competition's gate rules."""
    if not entry:
        raise ValueError("entry is empty")
    if entry != entry.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    if len(entry.strip()) == 0:
        raise ValueError("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.startswith("WARNING:"):
        raise ValueError("entry must start with the 'WARNING:' label prefix")
    if any(ord(ch) < 32 for ch in entry):
        raise ValueError("entry contains control characters")
    entry.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
