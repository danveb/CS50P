# Implement a Python program that prompts user for the name of variable in camel case ("helloWorld")
# output corresponding name in snake-case ("hello_world")

# test case:
## camelCase: name
## snake_case: name

## camelCase: firstName
## snake_case: first_name

# idx     0   1   2   3   4   5   6   7   8
# str     f   i   r   s   t   N   a   m   e
#         i                                   snake: f
#             i                               snake: fi
#                 i                           snake: fir
#                     i                       snake: firs
#                         i                   snake: first
#                             i               snake: first_n
#                                 i           snake: first_na
#                                     i       snake: first_nam
#                                         i   snake: first_name

def main():
    # prompt user for a camelCase variable
    user_input = input("camelCase: ")
    # return user input to snake_case
    print("snake_case:",convert_to_snake(user_input))

def convert_to_snake(str):
    """Converts given string into snake_case"""
    # initialize snake_str as empty str
    snake_str = ""
    # iterate over input string
    for character in str:
        # check: if character is an uppercase?
        # add "_" and also add its character in lowercase
        if character.isupper():
            snake_str += "_"
            snake_str += character.lower()
        # else we just keep adding characters to snake_str
        else:
            snake_str += character
    return snake_str

main()