"""The Meeting That Should Have Been an Email.

Writes one original funny line (at most 200 characters) about a meeting
that should have been an email, to /output/entry.txt.
"""

from pathlib import Path

LINE = (
    "The birthday committee met two hours to pick Brenda's cake, then "
    "sent one email ordering the exact cake Brenda bought herself last "
    "year."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
