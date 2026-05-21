import pytest

from app.shopping import get_total


def test_get_total_placeholder() -> None:
    with pytest.raises(NotImplementedError):
        get_total({}, [], 0.0)
