#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes one line of an out-of-office auto-reply, the funniest it can be,
140 characters at most, to /output/entry.txt. It reads like a real person
set it: they are away until Monday, and their cat is guarding the inbox —
and has already deleted three of the sender's emails.
"""

REPLY = (
    "I'm out of office until Monday. My cat has taken over my inbox and "
    "already deleted three of your emails. Send wisely."
)
LIMIT = 140
DEST = "/output/entry.txt"


def build_reply():
    text = REPLY.strip()
    assert text, "reply must not be empty"
    assert "\n" not in text, "reply must be a single line"
    assert len(text) <= LIMIT, f"reply is {len(text)} chars, over {LIMIT}"
    return text


def main():
    text = build_reply()
    with open(DEST, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(f"out-of-office written: {len(text)} chars")


if __name__ == "__main__":
    main()
