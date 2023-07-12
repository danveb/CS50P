# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# Example #2
# def main():
#     x = int(input("Enter x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# main()

# Example #3
def main():
    x = int(input("Enter X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(num):
    # this automatically returns True or False
    return True if num % 2 == 0 else False
    # return num % 2 == 0

main()