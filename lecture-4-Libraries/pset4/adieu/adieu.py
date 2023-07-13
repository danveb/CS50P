# Implement a Python program that prompts the user for names, one per line, until user inputs control-d
# assume user will input at least one name
# then bid "adieu" to those names, separating names with one AND, three names with two commas and one AND, and n-1 commas and one AND

import inflect

def main():
    # initialize inflect engine
    p = inflect.engine()
    # initialize empty []
    my_list = []

    while True:
        # try/except block
        try:
            # prompt user for input
            prompt = input("Name: ").strip()
            # append prompt to []
            my_list.append(prompt)
            output = p.join(my_list)
        except (EOFError, KeyError):
            print("\n")
            print("Adieu, adieu, to " + output)
            quit()

main()
