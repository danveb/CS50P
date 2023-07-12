# Loops in Python

# Loops
# - a loop is a way to repeat something over and over
# - loops enable us to create a block of code that executes over and over

# While Loop
# - we need to define a variable "i" with a value
# - "while" loop will keep running as long as we want
# - we need to set up a point where we can "break" out of the loop -> prevent an INFINITE LOOP

i = 0
while i <= 2:
    print("let's go!")
    i += 1

# For Loop
# - a for loop iterates through a "list" (array) of items []
# - we can use "i" to start iteration or just leave "_"

for i in [0, 1, 2]:
    print("hello")

for _ in range(2): # iterates 2 times
    print("bye")

# Improve User Input
# - we can use loops to validate input of the user
# - use "continue" and "break" keywords
# -> continue will go to next iteration
# -> break will break out of a loop

# List (ARRAY) []
# - a list is an unordered list of values in []

students = ["Hermione", "Harry", "Draco"]
houses = ["Griffyndor", "Griffyndor", "Slytherin"]

# iterate through a list?
# - use for IN loop

# check length of array?
# - len(array)

# Dictionaries
# - a data structure that allows us to associate keys with values

students = {
    "Hermione": "Griffyndor",
    "Harry": "Griffyndor",
    "Draco": "Slytherin",
}

# Nested Loops
