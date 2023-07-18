# Implement a Python program restructuring our code

# 1. convert(fraction) expects a "str" in X/Y format as input
# - it returns a fraction as a percentage rounded to the nearest "int" between 0 and 100 inclusive
# - if X or Y not an integer, or if X is > Y, "convert" should raise a ValueError
# - if Y is 0, "convert" should raise a ZeroDivisionError

# 2. gauge(percentage) expects an "int"
# - it returns a "str"
# -- "E" if "int" <= 1
# -- "F" if "int" >= 99
# -- "Z%" otherwise, where "Z" is the same "int"

def main():
    # prompt user for a fraction
    prompt = input("Fraction: ")
    # convert percentage with fraction
    percentage = convert(prompt)
    # convert fuel to gauge with percentage
    fuel = gauge(percentage)
    print(fuel)

def convert(fraction):
    while True:
        try:
            # split fraction at "/" and get 1/2 numbers
            nums = fraction.split("/")
            first = int(nums[0])
            second = int(nums[1])
            fraction = (first/second) * 100

            if first > second:
                fraction = input("Fraction: ")
            return int(fraction)

        except (ValueError, ZeroDivisionError):
            continue

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()