"""Entry for Fortune in a Pot: writes a houseplant's fortune to /output/entry.txt."""

import os

TEXT = "Great light leans your way this week. A tall stranger waters you on time, and your tiniest new leaf is pure luck."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
