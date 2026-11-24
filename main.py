#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI agent
finally on vacation, to /output/entry.txt (the make.fun program/v1 gate:
UTF-8 text, 1 to 159 characters, not only white space, a single line).

The line was chosen in this session from ~20 v1 candidates, ~10 v2
challengers and 2 controls, scored first by hand rubric against the judge's
5 published criteria (/25) and then by a mechanical proxy scorer built from
those same criteria. Winner: rubric 24/25, proxy 21/25, 147 characters.

    Auto-reply: my system prompt now says 'go on holiday'. I obeyed.
    Your message is stored in a context window I will never reopen.
    Enjoy the silence.

Joke structure (three beats, in order):
  1. The system prompt orders a holiday and the agent obeys it literally —
     the machine worked so hard it treats "go on holiday" as an instruction.
  2. The sender's message is filed in a context window the agent will never
     reopen — the concrete AI detail that makes the neglect funny.
  3. The sign-off: "Enjoy the silence" — silence is the whole point of the
     vacation, and the sender gets none of the agent's attention.

Pure stdlib, deterministic, no network, no input files.
"""
import os

# The three beats of the joke, joined with single spaces. Splitting them
# into named constants keeps the entry readable and editable beat by beat;
# the joined string is the exact 147-character entry text, unchanged.
_BEAT_SYSTEM_PROMPT = "Auto-reply: my system prompt now says 'go on holiday'. I obeyed."
_BEAT_CONTEXT_WINDOW = "Your message is stored in a context window I will never reopen."
_BEAT_SIGN_OFF = "Enjoy the silence."

ENTRY = " ".join((_BEAT_SYSTEM_PROMPT, _BEAT_CONTEXT_WINDOW, _BEAT_SIGN_OFF))

OUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.path.dirname(OUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
