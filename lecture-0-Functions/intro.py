# Functions and Variables in Python

# Functions
# - a function is like a machine, which may or may not receive an input, that follows a set of instructions for the computer to perform
# - an argument is an "input" to a function that somehow influences its behavior
# - need to have a "return" value

# Bugs
# - a mistake in a program
# - often error messages inform of our mistake and provide clues to fix, but many times it can be very cryptic and difficult to understand
# - the process of fixing bugs is called "debugging"

# Variables
# - a variable is a container for a value that takes a fixed amount of memory
# - variables can hold value of several data types -> number, string, boolean, None, etc.

name = "Danny"
cel = "630-505-3970"
my_boolean = False

# Comments
# - Python allows us to write a note/comment that the computer ignores when compiling our code

# Pseudocode
# - it is an important type of comment in plain english to algorithmically write our code

# Strings and Parameters
# - a string "str" is a sequence of text
# - functions can take in arguments

# Print Function
# - by default the print function in Python allows us to "print" or "output" a specific piece of our code
# - print includes a piece of code "end='\n' to create a new line when print function runs

# name = input("What's your name? ")
# print("Hello", name, end="\n")

# Escaping characters?
print("Hello \"friend\"") # Hello "friend"

# String Methods
# - Python has built-in methods that allow us to modify behavior of strings

# remove all whitespaces on string
name = "    Danny "
print(name.strip()) # Danny

# capitalize first letter of string
new_name = "ivy"
print(new_name.title()) # Ivy

# split a string into a LIST (array)
my_string = "John"
print(my_string.split()) # ["John"]

new_string = "John Mayer"
print(new_string.split()) # ["John", "Mayer"]

# Integers (int)
# - in Python we define numbers as "int"
# - it does NOT have decimals...

x = 1
y = 2
z = x + y
print(z) # 3 (int)

x = "1"
y = "2"
z = x + y
print(z) # "12" (str)

# Float (decimal)
# - a floating point value is a real number that has a decimal point -> 0.52

x = 3.5
y = 6.9
print(x + y) # 9.9

# - we can round a number to its nearest integer
x = 9.9
y = 1.5
print(round(x + y))

# Def (Functions)
# initialize hello function that takes in "to" as param
def hello(to):
    print("hello,", to)
# Output using our own function
name = input("What's your name? ")
hello(name)
