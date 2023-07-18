from lines import read_file

def test_read_file():
    assert read_file("test_hello.py") == 2
    assert read_file("album.txt") == 1

def test_cannot_read_file():
    assert read_file("empty") == 0
