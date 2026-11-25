#!/usr/bin/env python3
"""Writes the funniest one-line out-of-office auto-reply.

The reply is a single line of at most 160 characters, written to
/output/entry.txt exactly as the competition gate expects.
"""

import os

REPLY = (
    "Out of office until Monday. My inbox is now run by my cat, "
    "who approved your request, deleted the proof, and went back to sleep."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(REPLY)


if __name__ == "__main__":
    main()
