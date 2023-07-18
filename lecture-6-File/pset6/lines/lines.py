# Implement a Python program that expects exactly 1 command-line argument, the name (or path) of a Python file
# output the number of lines of code in that file, excluding comments and blank lines
# if user doesn't specify 1 command-line argument OR the file's name doesn't end in ".py", OR if file doesn't exist, exit the system with error message

# $ python lines.py
# Too few command-line arguments

# $ python lines.py hello.py goodbye.py
# Too many command-line arguments

# $ python lines.py invalid_extension.txt
# Not a Python file

# $ python lines.py non_existent_file.py
# File does not exist

import sys
import os

def main():
    # check: if we pass two command-line argument
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check: if we don't pass command-line arguments
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    # check: if we pass one command-line argument
    elif len(sys.argv) == 2:
        document = sys.argv[1]
        # check: if document does not endswith ".py" we proceed
        if not document.endswith(".py"):
            sys.exit("Not a Python file")
        # check: if document does not exist in filesystem?
        elif not os.path.isfile(document):
            sys.exit("File does not exist")
        # finally... we run read_file function
        else:
            print(read_file(document))

def read_file(doc):
    # initialize line_original, line_ignored as 0
    line_original = 0
    line_ignored = 0

    # open document in "read" mode and automatically close it
    with open(doc, "r") as file:
        line_original = file.readlines()

    # iterate over line_original
    for line in line_original:
        # check if any "#", new line or whitespace
        if line.strip().startswith("#") or line.strip().startswith("\n")or line.isspace():
            # increase ignored lines by 1
            line_ignored += 1

    line_count_final = len(line_original) - line_ignored
    return line_count_final

if __name__ == "__main__":
    main()