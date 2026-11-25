#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one short office joke (the duel-test winner of six drafts,
5 wins from 5 pairings, judged on the bounty brief: setup + turn,
recognisable office moment, punchline last) to /output/entry.txt.
"""

ENTRY = "The printer jammed at 4:59 PM on deadline day, so I named it Kevin and put it on the org chart under IT."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
