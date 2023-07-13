# Implement a Python program that prompts a user for a fraction (formatted as X/Y)
# output a percentage rounded to the nearest integer
# if 1% or less? output "E"
# if 99% or more? output "F"
# checks: x or y not integer? or x > y or y = 0? prompt again

# x: integer
# y: integer

def main():
    fuel = get_user_input()
    fuel_gauge = calculate_percentage(fuel)
    if fuel_gauge >= 99:
        print("F")
    elif fuel_gauge <= 1:
        print("E")
    else:
        print(f"{fuel_gauge}%")

def get_user_input():
    while True:
        # prompt user for a fraction
        prompt = input("Fraction: ")
        # try/except/else block
        try:
            # split prompt at "/" and get 1st/2nd nums
            nums = prompt.split("/") # 1/4
            first = int(nums[0]) # 1
            second = int(nums[1]) # 4
            # print(first, second)
            result = first / second
            if first > second:
                prompt = input("Fraction: ")
            elif second == 0:
                prompt = input("Fraction: ")
            return result
        except (ValueError, ZeroDivisionError):
            prompt = input("Fraction: ")

def calculate_percentage(num):
    """Convert num to percentage"""
    formula = round(num * 100)
    return formula

main()