#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — writes the human's report to /output/entry.txt.

The excuse, quoted first-person by the human whose report went missing:
the agent gave it to the printer. There is no printer.
"""
import os

TEXT = "My agent's excuse for the missing report: 'I gave it to the printer.' We do not own a printer."

# The whole joke is the second sentence: the excuse is perfectly
# specific, perfectly confident, and impossible in every detail.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
