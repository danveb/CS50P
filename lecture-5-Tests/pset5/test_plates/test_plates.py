from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("HELLO") == True
    assert is_valid("OUTAHERE") == False
    assert is_valid("H") == False
    assert is_valid("veryveryverymuch") == False
    assert is_valid("58") == False
    assert is_valid("AAA22A") == False
    assert is_valid("17ABC") == False
    assert is_valid("abc100") == True
    assert is_valid("a0b1c2") == False