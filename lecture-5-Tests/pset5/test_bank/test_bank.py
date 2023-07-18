from bank import value

def test_value_case_insensitive():
    assert value("hello") == 0
    assert value("Hello World") == 0

def test_value_h():
    assert value("hi there") == 20
    assert value("how are you?") == 20

def test_value_other():
    assert value("What are you up to?") == 100
    assert value("My name is Danny") == 100