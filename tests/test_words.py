from app.words import build_word


def test_build_word_uses_indexed_letters() -> None:
    assert build_word(["yoda", "best", "has"]) == "yes"


def test_build_word_returns_empty_string_for_empty_input() -> None:
    assert build_word([]) == ""
