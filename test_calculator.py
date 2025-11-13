import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1

def test_is_positive(calc):
    assert calc.is_positive(5) is True
    assert calc.is_positive(-3) is False
    assert calc.is_positive(0) is None # esta es la nueva prueba 

def test_add_decimals(calc):
    assert calc.add(2.5, 3.7) == pytest.approx(6.2)



