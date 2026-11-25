import pytest
from fraction import Fraction

# Initialization tests

def test_initialization():
    f = Fraction(3, 4)

    assert f.numerator == 3
    assert f.denominator == 4


def test_negative_numerator():
    f = Fraction(-3, 4)

    assert f.numerator == -3
    assert f.denominator == 4


def test_zero_numerator():
    f = Fraction(0, 5)

    assert f.numerator == 0
    assert f.denominator == 1

# Validation tests

def test_invalid_numerator_type():
    with pytest.raises(TypeError):
        Fraction(2.5, 4)


def test_invalid_denominator_type():
    with pytest.raises(TypeError):
        Fraction(3, 4.5)


def test_zero_denominator():
    with pytest.raises(ValueError):
        Fraction(3, 0)


def test_negative_denominator():
    with pytest.raises(ValueError):
        Fraction(3, -4)

# Simplification tests

def test_simplification():
    f = Fraction(12, 18)

    assert f.numerator == 2
    assert f.denominator == 3


def test_negative_simplification():
    f = Fraction(-6, 8)

    assert f.numerator == -3
    assert f.denominator == 4

# Comparison tests

def test_equal():
    assert Fraction(1, 2) == Fraction(2, 4)
    assert not (Fraction(1, 2) == Fraction(3, 4))


def test_not_equal():
    assert Fraction(1, 2) != Fraction(3, 4)
    assert not (Fraction(1, 2) != Fraction(2, 4))

def test_less_than():
    assert Fraction(1, 2) < Fraction(3, 4)
    assert not (Fraction(3, 4) < Fraction(1, 2))
    assert not (Fraction(1, 2) < Fraction(2, 4))
    assert Fraction(-1, 2) < Fraction(1, 2)


def test_less_than_or_equal():
    assert Fraction(1, 2) <= Fraction(3, 4)
    assert not (Fraction(3, 4) <= Fraction(1, 2))
    assert Fraction(1, 2) <= Fraction(2, 4)
    assert Fraction(-1, 2) <= Fraction(1, 2)

def test_greater_than():
    assert Fraction(3, 4) > Fraction(1, 2)
    assert not (Fraction(1, 2) > Fraction(3, 4))
    assert not (Fraction(1, 2) > Fraction(2, 4))
    assert Fraction(1, 2) > Fraction(-1, 2)


def test_greater_than_or_equal():
    assert Fraction(3, 4) >= Fraction(1, 2)
    assert not (Fraction(1, 2) >= Fraction(3, 4))
    assert Fraction(1, 2) >= Fraction(2, 4)
    assert Fraction(1, 2) >= Fraction(-1, 2)

# Addition tests

def test_addition():
    result = Fraction(1, 2) + Fraction(1, 3)

    assert result.numerator == 5
    assert result.denominator == 6


def test_addition_simplification():
    result = Fraction(1, 4) + Fraction(1, 4)

    assert result.numerator == 1
    assert result.denominator == 2

# Subtraction tests

def test_subtraction():
    result = Fraction(3, 4) - Fraction(1, 2)

    assert result.numerator == 1
    assert result.denominator == 4


def test_negative_subtraction():
    result = Fraction(1, 2) - Fraction(3, 4)

    assert result.numerator == -1
    assert result.denominator == 4


def test_subtraction_zero():
    result = Fraction(3, 4) - Fraction(3, 4)

    assert result.numerator == 0
    assert result.denominator == 1

# Multiplication tests

def test_multiplication():
    result = Fraction(2, 3) * Fraction(3, 4)

    assert result.numerator == 1
    assert result.denominator == 2


def test_negative_multiplication():
    result = Fraction(-2, 3) * Fraction(3, 4)

    assert result.numerator == -1
    assert result.denominator == 2


def test_multiplication_zero():
    result = Fraction(2, 3) * Fraction(0, 5)

    assert result.numerator == 0
    assert result.denominator == 1

# Division tests

def test_division():
    result = Fraction(2, 3) / Fraction(4, 5)

    assert result.numerator == 5
    assert result.denominator == 6


def test_negative_division():
    result = Fraction(2, 3) / Fraction(-4, 5)

    assert result.numerator == -5
    assert result.denominator == 6


def test_zero_divided_by_fraction():
    result = Fraction(0, 1) / Fraction(2, 3)

    assert result.numerator == 0
    assert result.denominator == 1


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        Fraction(2, 3) / Fraction(0, 1)