from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size == 11

    with pytest.raises(ValueError):
        jar.deposit(33)

def test_widthdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7

    with pytest.raises(ValueError):
        jar.withdraw(669)