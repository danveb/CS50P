import sys

# print(sys.argv[0]) # name_of_program.py
# print(sys.argv[1]) # argument_after_name_of_program

# Example 1
# print the string with its argument vector [1]
# print("hello my name is", sys.argv[1])
# $ python name.py Danny
# hello my name is Danny

# $ python name.py
# IndexError: list index out of range -> we don't pass arguments after name_of_program

# - how to deal with potential errors?
# -- try/except block

# Example 2
# try:
#     print("Hello my name is", sys.argv[1])
# except:
#     print("Too few arguments")

# $ python name.py Danny
# Hello my name is Danny

# $ python name.py
# Too few arguments

# - another way to deal with errors?
# -- we can perform conditional checks

# Example 3

# check: if length of system arguments is 1
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello my name is", sys.argv[1])

# $ python name.py Danny
# Hello my name is Danny

# $ python name.py Danny Kels
# Too many arguments

# $ python name.py
# Too few arguments

# $ python name.py "Danny Kels" -> Python recognizes this as 1 argument
# Hello my name is Danny Kels

# Example 4 -> after conditional checking we could potentially get another Error...
# check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# # print name tag
# print("Hello my name is", sys.argv[1])

# Example 5 -> use "sys.exit" to exit the program after conditionally checking
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
print("Hello my name is", sys.argv[1])

