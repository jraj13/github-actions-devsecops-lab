import pytest

from secure_app.app import calculate_total


def test_calculate_total() -> None:
    assert calculate_total(100.0, 0.07) == 107.0


def test_zero_tax() -> None:
    assert calculate_total(100.0, 0.0) == 100.0


def test_negative_amount_fails() -> None:
    with pytest.raises(ValueError, match="amount must be non-negative"):
        calculate_total(-1.0, 0.07)


def test_negative_tax_rate_fails() -> None:
    with pytest.raises(ValueError, match="tax_rate must be non-negative"):
        calculate_total(100.0, -0.01)
