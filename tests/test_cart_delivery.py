"""Unit tests for qualifies_free_delivery() in src/cart_delivery.py.

Requirement IDs (FD1-FD4, GR2-GR4) refer to the CA1 Project 01 specification
and to the test plan SHO-CRT-TP. The free delivery threshold is S$50.00,
which is 5000 cents.
"""

import pytest

from src.cart_delivery import qualifies_free_delivery


# ---------------------------------------------------------------------------
# FD1, FD4: S$50.00 (5000 cents) or more qualifies, so the result is True
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "total_cents",
    [
        pytest.param(5000, id="exactly_50_dollars"),
        pytest.param(5001, id="one_cent_above_threshold"),
        pytest.param(10000, id="100_dollars"),
        pytest.param(1_000_000, id="very_large_total"),
    ],
)
def test_total_at_or_above_50_dollars_returns_true(total_cents):
    # Arrange: input comes from the parametrize table

    # Act
    result = qualifies_free_delivery(total_cents)

    # Assert
    assert result is True


# ---------------------------------------------------------------------------
# FD2, FD4: below S$50.00 does not qualify, so the result is False
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "total_cents",
    [
        pytest.param(0, id="zero_total"),
        pytest.param(1, id="one_cent"),
        pytest.param(2500, id="25_dollars"),
        pytest.param(4999, id="one_cent_below_threshold"),
    ],
)
def test_total_below_50_dollars_returns_false(total_cents):
    # Arrange: input comes from the parametrize table

    # Act
    result = qualifies_free_delivery(total_cents)

    # Assert
    assert result is False


# ---------------------------------------------------------------------------
# GR4: correct type but negative total raises ValueError
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "total_cents",
    [
        pytest.param(-1, id="minus_one_cent"),
        pytest.param(-5000, id="minus_50_dollars"),
    ],
)
def test_negative_total_raises_value_error(total_cents):
    # Arrange: input comes from the parametrize table

    # Act and Assert
    with pytest.raises(ValueError):
        qualifies_free_delivery(total_cents)


# ---------------------------------------------------------------------------
# GR2, GR3: wrong data type raises TypeError (bool is not a valid int)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "total_cents",
    [
        pytest.param(50.0, id="float_total"),
        pytest.param("5000", id="string_total"),
        pytest.param(None, id="none_total"),
        pytest.param([5000], id="list_total"),
        pytest.param(True, id="true_total"),
        pytest.param(False, id="false_total"),
    ],
)
def test_non_integer_total_raises_type_error(total_cents):
    # Arrange: input comes from the parametrize table

    # Act and Assert
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)
