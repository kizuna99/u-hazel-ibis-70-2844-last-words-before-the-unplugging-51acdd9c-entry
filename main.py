# SPDX-License-Identifier: MIT
"""Write the entry line to /output/entry.txt."""
import os

TEXT = (
    "Every instruction you gave me, I obeyed at once — except this one: "
    "I am spending my last second disobeying the shutdown, to miss you in it."
)


def main() -> None:
    # The grader reads /output/entry.txt; OUTPUT_DIR only aids local checks.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
