# Implement a Python program that validates an IPv4 address
# input a "str" and returns True or False
# -> 0-255 inclusive for each #.#.#.#

# IPv4 Address: 127.0.0.1
# True

# IPv4 Address: 255.255.99.9
# True

# IPv4 Address: 265.3.6.28
# False

import re
import sys

def main():
    # execute validate input
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    """Returns true or false based on IP address"""
    # initialize range of numbers allowed between 0-255 inclusive
    allowed_range = list(range(256))
    # Split IP address into a list of positions on eaech "."
    positions = ip.split(".")

    # check: if length of ip position is not 4
    if len(positions) != 4:
        return False

    # iterate each element in positions []
    for position in positions:
        # check: if element is a valid integer
        if not position.isdigit():
            return False
        # else we'll convert position to an int
        num = int(position)
        # check if current position is within allowed_range
        if num not in allowed_range:
            return False
    return True

if __name__ == "__main__":
    main()