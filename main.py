"""Vacuum's alibi — one-line excuse entry.

Writes one fixed sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The sentence is the robot vacuum's sensor log: at 14:02 an unidentified
crumb, at 14:03 the crumb has a lawyer. Deadpan machine voice, a one-minute
escalation as the surprise, and "Case closed" as the punch at the end.

Revision: docstring now names the one-minute escalation explicitly; the
entry sentence itself is unchanged (still 90 characters, sha256 81b50e76...).
"""

import os
from pathlib import Path

TEXT = (
    "Sensor log, 14:02: unidentified crumb. "
    "Sensor log, 14:03: crumb has a lawyer. Case closed."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
