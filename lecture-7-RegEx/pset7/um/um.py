# Implement a Python program that expects a line of text as input "str"
# outputs an "int", the number of times that "UM" appears in that text, case-insensitively
# - if "um" appears in text we return 1
# - if "um" appears as substring we return 0

import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # match_case "um"
    um_list = re.findall(r"\bum\b", s, re.IGNORECASE)
    # print(um_list)
    return(len(um_list))

if __name__ == "__main__":
    main()