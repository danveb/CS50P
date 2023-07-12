# print("#")
# print("#")
# print("#")

# for loop?
# for _ in range(3):
#     print("#")
#     # #
#     # #
#     # #

# function?
def main():
    return print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# another function?
def main():
    return print_row(4)

def print_row(width):
    for _ in range(width):
        print("?" * width)

main()

# another function?
def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")
        # print a blank line
        print()

main()

# better?
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()