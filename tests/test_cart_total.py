"""Unit tests for calculate_total() in src/cart_total.py.

Requirement IDs (CT1-CT3, GR2-GR4) refer to the CA1 Project 01 specification
and to the test plan SHO-CRT-TP.
"""

import pytest

from src.cart_total import calculate_total


# ---------------------------------------------------------------------------
# CT1, CT3: total = unit price x quantity, returned in cents
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "unit_price_cents, quantity, expected_total",
    [
        pytest.param(100, 1, 100, id="quantity_one_returns_unit_price"),
        pytest.param(250, 3, 750, id="several_items_returns_price_times_quantity"),
        pytest.param(1, 1, 1, id="smallest_positive_price_and_quantity"),
        pytest.param(999, 100, 99900, id="large_quantity"),
    ],
)
def test_valid_price_and_quantity_returns_product_in_cents(
    unit_price_cents, quantity, expected_total
):
    # Arrange: inputs come from the parametrize table

    # Act
    result = calculate_total(unit_price_cents, quantity)

    # Assert
    assert result == expected_total
    assert type(result) is int


# ---------------------------------------------------------------------------
# CT2: a unit price or quantity of zero gives a total of zero
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        pytest.param(0, 5, id="zero_price"),
        pytest.param(100, 0, id="zero_quantity"),
        pytest.param(0, 0, id="zero_price_and_zero_quantity"),
    ],
)
def test_zero_price_or_zero_quantity_returns_zero(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize table

    # Act
    result = calculate_total(unit_price_cents, quantity)

    # Assert
    assert result == 0


# ---------------------------------------------------------------------------
# GR4: correct type but negative value raises ValueError
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        pytest.param(-1, 1, id="negative_price"),
        pytest.param(100, -1, id="negative_quantity"),
        pytest.param(-1, -1, id="negative_price_and_negative_quantity"),
    ],
)
def test_negative_price_or_quantity_raises_value_error(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize table

    # Act and Assert
    with pytest.raises(ValueError):
        calculate_total(unit_price_cents, quantity)


# ---------------------------------------------------------------------------
# GR2, GR3: wrong data type raises TypeError (bool is not a valid int)
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        pytest.param(10.5, 1, id="float_price"),
        pytest.param("100", 1, id="string_price"),
        pytest.param(None, 1, id="none_price"),
        pytest.param(True, 1, id="true_price"),
        pytest.param(False, 1, id="false_price"),
        pytest.param(100, 2.0, id="float_quantity"),
        pytest.param(100, "2", id="string_quantity"),
        pytest.param(100, None, id="none_quantity"),
        pytest.param(100, True, id="true_quantity"),
        pytest.param(100, False, id="false_quantity"),
    ],
)
def test_non_integer_price_or_quantity_raises_type_error(unit_price_cents, quantity):
    # Arrange: inputs come from the parametrize table

    # Act and Assert
    with pytest.raises(TypeError):
        calculate_total(unit_price_cents, quantity)
