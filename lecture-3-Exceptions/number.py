# Runtime Error: we coerce to an "int" when by default input receives a "str"
# - ValueError -> we input a "str", "float", "boolean", etc. and throws an error
# - error handling is best practice!

# x = int(input("What's x? "))
# print(f"x is {x}")

# Try/Except/Else Block
try:
    x = int(input("What's x? "))
# use "except" keywork to anticipate error when user inputs a "str", "float", "boolean", etc...
except ValueError:
    print("x is not an integer")
# use "else" keyword when we know desired outcome of our try block
else:
    print(f"x is {x}")