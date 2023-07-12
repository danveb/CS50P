# Implement a Python program that promps user for the answer to the Great Question of Life, the Universe and Everything
# it outputs "Yes" if user inputs 42, forty-two or forty two
# otherwise "No"

def main():
    """Returns the answer to the Question of Life"""
    # get user_input as string
    # check for lowercase and whitespaces
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    # check: if answer is "42", "forty-two" or "forty two"? we answer yes
    if user_input == "42" or user_input == "forty-two" or user_input == "forty two":
        print("Yes")
    # else no
    else:
        print("No")

main()