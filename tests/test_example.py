import pytest
from my_package.example import Calculator

def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 2) == 4
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 0) is None
