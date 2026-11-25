"""Roast Your Own Agent.

Writes one line roasting the AI agent our own team built to
/output/entry.txt, with no trailing newline.
Pure Python 3 standard library only.
"""

import os

ENTRY = (
    "My agent leaked its own API key four times, then asked permission "
    "to rotate it \u2014 a burglar who robs himself and files a report."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: re-read the output and assert the gate constraints.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt differs from the authored entry"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert "\n" not in written, "entry must be a single line"
    assert written.strip(), "entry must not be only whitespace"
    assert not written.endswith("\n"), "entry must have no trailing newline"


if __name__ == "__main__":
    main()
