from numb3rs import validate

def test_validate_true():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.1") == True

def test_validate_false():
    assert validate("256.0.0.1000") == False
    assert validate("1.1.1") == False
    assert validate("cat") == False
    assert validate("1.490.256.255") == False
    assert validate("268.0.6.7") == False
