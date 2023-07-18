from hello import hello

def test_default():
    assert hello() == "Hello world"

def test_argument():
    for name in ["Hermione", "Harry", "Draco"]:
        assert hello(name) == f"Hello {name}"
    assert hello("David") == "Hello David"
