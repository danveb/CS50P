# Implement a Python program that expects 1 command-line argument, name (or path) of a CSV file
# output a table formatted as ASCII art using "tabulate" package on PyPI
# format the table using "grid" format
# - if user does NOT specify 1 command-line argument, or if the specified file's name does NOT end in ".csv" or if file does NOT exist, sys.exit()!

import os
import sys
import csv
from tabulate import tabulate

def main():
    # check: if no command-line arguments (len == 1)
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check: if too many command-line arguments
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check: if it's at least 1 command-line argument (len == 2)
    elif len(sys.argv) == 2:
        # get document from command-line argument
        document = sys.argv[1]
        # print(document)
        # check: if document does NOT endwith ".csv"
        if not document.endswith(".csv"):
            sys.exit("Not a CSV file")
        # check: if document does not exist in filesystem
        elif not os.path.isfile(document):
            sys.exit("File does not exist")
        # we proceed to read the CSV
        else:
            return read_csv(document)

def read_csv(doc):
    # table = []
    table = []
    # open a CSV document as file
    with open(doc) as file:
        # initialize reader as csv.DictReader
        reader = csv.DictReader(file)
        # tabulate csv table, headers and format as "grid"
        print(tabulate(reader, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()