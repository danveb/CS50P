from twttr import shorten

def test_shorten():
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("What a beautiful day") == "Wht  btfl dy"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("My sweet h0me!") == "My swt h0m!"