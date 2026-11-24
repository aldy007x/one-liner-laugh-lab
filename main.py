#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

The prompt: the excuse a robot vacuum gives after eating a sock.
This program writes one short funny line (at most 200 characters)
to /output/entry.txt, where the house judge reads it.
"""

import os

LINE = "I didn't eat the sock. I promoted it: it's middle management in my dustbin now."


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if len(line) > 200:
        raise SystemExit(f"line is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")

    out_dir = "/output" if os.path.isdir("/output") else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} characters to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
