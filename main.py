"""Museum of the Year 3000 — entry program.

Writes the museum label (one line, at most 200 characters) to
/output/entry.txt and prints it to stdout.

The label is a museum label from the year 3000 for an ordinary object
from today — a smoke detector, misread as a ceiling oracle that
screamed at cooked food and was honoured by having its batteries
removed. Deterministic: the same line is written on every run, with
no input, randomness, or network access.
"""

import os

LINE = "Ceiling oracle, c. 2024. It screamed whenever food was cooked; families honoured it by removing its batteries."

assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert "\n" not in LINE and "\r" not in LINE, "entry line must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Exactly one line plus a single trailing newline, nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Read back and confirm the file holds exactly the entry line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n", "entry file does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
