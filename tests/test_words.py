import pytest

from app.words import build_word


def test_build_word_placeholder() -> None:
    with pytest.raises(NotImplementedError):
        build_word([])
