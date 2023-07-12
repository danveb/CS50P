# print("Meow")
# print("Meow")
# print("Meow")

# # While Loop
# i = 3
# while i != 0:
#     print("Meow")
#     i = i - 1
# # Meow Meow Meow

# i = 1
# while i <= 3:
#     print("meow")
#     i += 1
# # meow meow meow

# i = 0
# while i < 3:
#     print("hellow")
#     i += 1
# # hellow hellow hellow

# # For Loop
# for i in [0, 1, 2]:
#     print("melon")
# # melon melon melon

# for i in range(3):
#     print("uva")
# # uva uva uva

# for _ in range(3):
#     print("grape")
# # grape grape grape

# Input Validation
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# As Function
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter n: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()