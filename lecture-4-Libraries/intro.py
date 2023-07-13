# Libraries

# Libraries are programs written by others that we can use to perform more code
# - a module contains functions for reusability of code
# -> ex: "random" module

random.choice(sequence[])

# - we can import specific functions from a module
# - allows our program to run faster because we don't run ALL functions from a library
# -> ex: from random import choice

from random import choice, randint

import statistics

statistics.mean(sequence[])

# Command Line Arguments
# - allows us to provide "arguments" when executing a command-line prompt
# -> ex: python average.py 100 90 (100, 90) are the arguments here!

# print(sys.argv[0]) # name_of_program.py
# print(sys.argv[1]) # argument_after_name_of_program

import sys
# print the string with its argument vector [1]
print("hello my name is", sys.argv[1])
# $ python name.py Danny
# hello my name is Danny

# - how to deal with potential errors?
# -- try/except block
# -- conditional checking on length of sys.argv

# Slice
# - we can slice a list in a particular way
# - NOTE: we can slice up to, and NOT including, a specific index
house = ["LA", "Irvine", "Chicago"]
# print(house[0]) # slice 0th index # LA
# print(house[1]) # slice 1st index # Irvine
# print(house[1:]) # slice from 1st index to no end # ["Irvine", "Chicago"]
print(house[1:-1]) # slice from 1st index to -1 index, which is counting to left # ["Irvine"]
print(house[0:2]) # slice from 0th index to 2nd index NOT inclusive # ["LA", "Irvine"]

# Packages
# - Python comes with third-party packages (libraries) that add functionality
# -> Pypi is a repo of all available 3rd party packages
# -> "cowsay" is a package that allows a cow to talk to the user

# Pip
# - pip is Python's package manager that allows to install packages into the system
# $ pip install cowsay

# API
# - application programming interface that we can connect to use code of others
# - "requests" is a package that allows our program to behave as a web browser to make HTTP REQUESTS
# $ pip install requests

# JSON
# - javascript object notation, a text-based format we receive when making HTTP requests
# - python has a built-in JSON library to help interpret JSON received
import json

