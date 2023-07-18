from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100

    # ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    # ValueError
    with pytest.raises(ValueError):
        convert("x/y")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(84) == "84%"
    assert gauge(1) == "E"
