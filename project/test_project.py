from project import check_length, check_capitalize, memefy
import os
import pytest


def test_check_length():
    assert check_length("Hello World") == "Hello World"
    assert check_length("I DON'T KNOW WHAT THIS MEANS") == "I DON'T KNOW WHAT THIS MEANS"

    # check for sys.exit on surpassing max character limit
    with pytest.raises(SystemExit) as exc_info:
        check_length("This is a very very long text that exceeds the character limit imposed by memefy python program and will throw an error message and exit automatically")
    assert str(exc_info.value) == "Over 40 characters... please consider shortening it"

    # check for sys.exit below min threshold of characters
    with pytest.raises(SystemExit) as exc_info:
        check_length("Bye")
    assert str(exc_info.value) == "Minimum 5 characters..."


def test_check_capitalize():
    assert check_capitalize("Hello World") == "HELLO WORLD"
    assert check_capitalize("what are you doing?") == "WHAT ARE YOU DOING?"
    assert check_capitalize("what! are you $aying?") == "WHAT! ARE YOU $AYING?"

def test_memefy():
    # initialize top/bottom text
    top_text = "Hello World"
    bottom_text = "I don't know what this means"
    # instantiate output_file
    output_file = memefy(top_text, bottom_text)
    # check if output file exists
    assert os.path.exists(output_file)
    # check if output file extension is .jpg
    assert os.path.splitext(output_file)[1] == ".jpg"
    # clean up after done testing
    os.remove(output_file)

