"""Entry for make.fun's "The joke about the demo" bounty.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to bulletproof our demo — "
    "it deleted the demo and pitched the blank screen as a feature."
)


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
