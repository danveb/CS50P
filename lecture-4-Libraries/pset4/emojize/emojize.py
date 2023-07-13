# Implement a program that promps the user for a "str"
# output the "emojized" version, converting any codes/aliases to corresponding emoji

# Input: :thumbs_up:
# Output: 👍

# Input: :mate:
# Output: 🧉

import emoji

def main():
    # prompt user to input a "str"
    prompt = input("Input: ")
    # emojize user prompt and print it
    emojized = emoji.emojize(prompt, language="alias")
    print(f"Output: {emojized}")

main()