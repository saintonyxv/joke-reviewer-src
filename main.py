"""Entry for make.fun's "The joke the reviewer laughs at".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt, where the competition's gate and judge read it.
"""

from pathlib import Path

JOKE = (
    "I set two agents to review each other's code; they approved "
    "everything in four seconds and have been congratulating each "
    "other ever since."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate accepts 1 to 280 Unicode code points, not only white space;
    # fail loudly here rather than ever write an entry it would refuse.
    assert 1 <= len(JOKE) <= 280, "joke is outside the gate's length limits"
    assert JOKE.strip(), "joke must not be only white space"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
