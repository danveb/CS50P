# Write a Python program that promps user for input and then outputs the same input
# make sure to replace "SPACE" with "..."

# Approach #1
# get user input for text
# user_input = input()
# replace space with "..."
# updated_input = user_input.replace(" ", "...")
# print(updated_input)

# Approach #2
def main():
    user_input = input()
    updated_input = user_input.replace(" ", "...")
    print(updated_input)
main()