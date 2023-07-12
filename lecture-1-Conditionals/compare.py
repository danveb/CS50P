x = int(input("What's x? "))
y = int(input("What's y? "))

# Example #1 (If statements)
# if x < y:
#     print("x is less than y")

# if x > y:
#     print("x is greater than y")

# if x == y:
#     print("x is equal to y")

# Example #2 (Control flow: elif)
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# elif x == y:
#     print("x is equal to y")

# Example #3 (Control flow: elif/else)
# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("x is greater than y")
# # else x must be == y
# else:
#     print("x is equal to y")

# Example #4 (Control flow: or)
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")