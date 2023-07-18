from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("My Good Fellow") == 0
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("yum! I want to eat durian again") == 0
    assert count("Um, thanks, um...") == 2