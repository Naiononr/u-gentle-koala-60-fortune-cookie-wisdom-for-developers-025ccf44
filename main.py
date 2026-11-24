"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original line of fortune-cookie wisdom for a software
developer to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, deterministic, no network, no randomness.
"""

import os

LINE = "The bug will confess the moment you explain it aloud to someone who is not listening."


def main():
    # Gate check, mirroring the sealed scorer: 1-120 chars, one line.
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} chars, must be 1-120"
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
