from calculator import square

def main():
    """Tests square function"""
    test_square()

def test_square():
    # manually check if square(2) is NOT equal to 4
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(3) != 9:
    #     print("3 squared was not 9")
    # if square(4) != 16:
    #     print("4 squared was not 16")

    # use assertion
    # assert square(2) == 4
    # assert square(3) == 9

    # assert with try/except block
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")

    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

if __name__ == "__main__":
    main()