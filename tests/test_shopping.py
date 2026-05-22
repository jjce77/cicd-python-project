from app.shopping import get_total


def test_get_total_ignores_missing_items_and_applies_tax() -> None:
    costs = {"socks": 5, "shoes": 60, "sweater": 30}

    assert get_total(costs, ["socks", "shoes"], 0.08) == 70.2


def test_get_total_returns_zero_when_no_items_exist() -> None:
    assert get_total({"socks": 5}, ["hat"], 0.08) == 0.0

