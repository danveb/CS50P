# Implement a Python program that prompts user for an arithmetic expression
# calculate and output the result as a floating-point value formatted to 1 decimal place
# x: integer
# y: operation + - * /
# z: integer

def main():
    """Perform an arithmetic expression returning a float"""
    # prompt user for an input; use x, y, z
    x, y, z = input("Expression: ").strip().split(" ")
    # return calculation
    print(f"{calculation(int(x), str(y), int(z)):.1f}")

def calculation(x, y, z):
    """Calculations based on operation"""
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

main()