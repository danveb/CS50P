# Calculator app

# Example #1 -> calculator for "string" because we're concatenating strings
# get user input for x and y
x = input("What's x? ") # 10
y = input("What's y? ") # 20
z = x + y
print(z) # 1020

# Example #2 -> calculator for "int"
# - we can use "type casting" where we explicitly define the return of input is an "INT"
x = int(input("What's x? ")) # 10
y = int(input("What's y? ")) # 20
z = x + y
print(z) # 30

# Example #3 -> calculator for "float"
x = float(input("What's x? ")) # 9.9
y = float(input("What's y? ")) # 1.1
print(x + y) # 11.0

# Example #4 -> calculator with "round"
x = float(input("What's x? ")) # 9.9
y = float(input("What's y? ")) # 3.6
print(round(x + y)) #13.5 -> 14

# Example #5 -> calculator with "round"
# Get the user's input
x = float(input("What's x? ")) # 3000
y = float(input("What's y? ")) # 5000
# Create a rounded result
z = round(x + y) # 8000
# Print the formatted result
print(f"{z:,}") # 8,000