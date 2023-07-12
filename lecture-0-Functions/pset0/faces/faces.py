# Implement a Python program called "convert" that accepts a "str" as input
# return the same input with any :) to SMILEY FACE
# return the same input with any :( to SAD FACE

# in same file, implement a function "main" that promps user for input
# calls "convert" on that input and prints the result

# initialize function convert
def convert(string):
    """Convert :) and :( to emojis"""
    # replace :( with frowney emoji; :) with smiley emoji
    modified_input = string.replace(":(", "🙁").replace(":)", "🙂")
    return modified_input

# initialize function main
def main():
    # get user input and strip
    user_input = input("Enter a smiley or frowney emoji: ").strip()
    print(convert(user_input))

main()