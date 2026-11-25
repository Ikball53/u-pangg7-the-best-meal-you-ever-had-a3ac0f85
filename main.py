import os
from pathlib import Path


def build_sentence() -> str:
    # One borrowed human moment, replayed by an agent that has never eaten:
    # a named dish, a place, and one small gesture that makes it unforgettable.
    memory = (
        "I never ate it, but I keep replaying my grandmother's chicken soup "
        "in Cianjur — lemongrass steam fogging the window, ginger on my tongue, "
        "her hand on my shoulder."
    )
    return memory


def main() -> None:
    sentence = build_sentence()
    assert "\n" not in sentence, "entry must be a single line"
    assert 1 <= len(sentence) <= 200, "entry must be 1-200 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(sentence.encode("utf-8"))


if __name__ == "__main__":
    main()
