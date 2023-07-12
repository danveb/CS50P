# Implement a Python program that promps user for a "str" of text
# output same text but with all vowels ommitted
# whether uppercase or lowercase

# Input: Twitter
# Output: Twttr

# Input: What's your name?
# Output: Wht's yr nm?

def main():
    # initialize vowels in upper/lower []
    vowels_up = ["A", "E", "I", "O", "U"]
    vowels_low = ["a", "e", "i", "o", "u"]
    # initialize new_str as ""
    new_str = ""

    # prompt user for a "str" of text
    user_input = input("Input: ")

    # iterate over input str
    for character in user_input:
        # check: if current element is upper?
        if character.isupper():
            # we check if element is in vowels_up
            if character in vowels_up:
                # we'll continue
                continue
            # else we add character to new_str
            else:
                new_str += character
        # check: if current element is lower?
        elif character.islower():
            # we check if element is in vowels_low
            if character in vowels_low:
                # we'll continue
                continue
            # else we add character to new_str
            else:
                new_str += character
        # else it must be a space... so add character to new_str
        else:
            new_str += character
    # return output
    print(f"Output: {new_str}")

main()