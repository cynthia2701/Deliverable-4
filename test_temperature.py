import pytest
from temperature import Temperature

# 1. Initialization

def test_default_unit():
    temp = Temperature(25)
    assert temp.value == 25.0
    assert temp.unit == "C"


def test_case_insensitive_units():
    assert Temperature(25, "c").unit == "C"
    assert Temperature(77, "f").unit == "F"
    assert Temperature(300, "k").unit == "K"


def test_read_only_attributes():
    temp = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"

# 2. Validation

def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")


def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-274, "C")

    with pytest.raises(ValueError):
        Temperature(-460, "F")

    with pytest.raises(ValueError):
        Temperature(-1, "K")


def test_invalid_target_unit():
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to("X")

# 3. Conversions

@pytest.mark.parametrize("c, f, k", [
    (-273.15, -459.67, 0),
    (-40, -40, 233.15),
    (0, 32, 273.15),
    (37, 98.6, 310.15),
    (100, 212, 373.15)
])
def test_conversions(c, f, k):
    temp_c = Temperature(c, "C")
    temp_f = Temperature(f, "F")
    temp_k = Temperature(k, "K")

    assert temp_c.to_fahrenheit() == pytest.approx(f, abs=1e-9, rel=0)
    assert temp_c.to_kelvin() == pytest.approx(k, abs=1e-9, rel=0)

    assert temp_f.to_celsius() == pytest.approx(c, abs=1e-9, rel=0)
    assert temp_f.to_kelvin() == pytest.approx(k, abs=1e-9, rel=0)

    assert temp_k.to_celsius() == pytest.approx(c, abs=1e-9, rel=0)
    assert temp_k.to_fahrenheit() == pytest.approx(f, abs=1e-9, rel=0)

# 4. Round-trip conversions

def test_round_trip():
    original = Temperature(25, "C")

    fahrenheit = original.convert_to("F")
    kelvin = fahrenheit.convert_to("K")
    celsius = kelvin.convert_to("C")

    assert celsius.unit == "C"
    assert celsius.value == pytest.approx(
        original.value, abs=1e-9, rel=0
    )
    assert celsius == original

# 5. Cross-unit comparisons

def test_equality():
    assert Temperature(0, "C") == Temperature(32, "F")
    assert Temperature(0, "C") == Temperature(273.15, "K")


def test_not_equal():
    assert Temperature(0, "C") != Temperature(100, "F")


def test_less_than():
    assert Temperature(0, "C") < Temperature(300, "K")


def test_less_than_or_equal():
    assert Temperature(0, "C") <= Temperature(32, "F")
    assert Temperature(0, "C") <= Temperature(300, "K")


def test_greater_than():
    assert Temperature(100, "C") > Temperature(32, "F")


def test_greater_than_or_equal():
    assert Temperature(0, "C") >= Temperature(32, "F")
    assert Temperature(100, "C") >= Temperature(300, "K")

# 6. Formatting

def test_str():
    temp = Temperature(25, "C")
    assert str(temp) == "25.00 °C"


def test_repr():
    temp = Temperature(25, "C")
    assert repr(temp) == "Temperature(25.0, 'C')"