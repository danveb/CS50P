# Restructure existing code
# "shorten" expects a "str" as input
# it returns the same "str" but with all vowels ommitted, where uppercase or lowercase

# Input: Twitter
# Output: Twttr

# Input: What's your name?
# Output: Wht's yr nm?

def main():
    # prompt user for a string of text
    prompt = input("Input: ")
    # print the shortened string
    print(shorten(prompt))

def shorten(word):
    # initialize vowels in upper/lower []
    all_vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    # initialize new_str as ""
    new_str = ""

    # iterate character in word
    for character in word:
        # check if character not in all_vowels
        if character not in all_vowels:
            # build new_str
            new_str += character

    return new_str

if __name__ == "__main__":
    main()