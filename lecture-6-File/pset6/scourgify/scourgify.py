# Implement a Python program:
# - expect user to provide 2 command-line arguments -> len(sys.argv) == 3
# -- name of csv file to read as input, columns "name" and "house"
# -- name of csv file to write as output, columns "first", "last", "house"
# - convert input to output, splitting each "name" into "first" and "last" name
# if a user does not provide 2 command-line arguments, or if the first csv cannot be read, the program exits with an error message

import os
import sys
import csv

def main():
    # check: if user provides < 1 command-line argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check: if user provides > 3 command-line arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check: if user provides 2 command-line arguments
    else:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        # check: if document1 cannot be read?
        if not os.path.isfile(read_file):
            sys.exit(f"Could not read {read_file}")
        # check: if document1 does not end with ".csv"
        elif not read_file.endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            return read_and_write(read_file, write_file)

def read_and_write(read_file, write_file):
    """Reads CSV and Writes CSV"""
    # open csv file in "read" mode
    with open(read_file, "r") as read:
        # initialize csv.DictReader on read file
        reader = csv.DictReader(read)

        # open csv file in "write" mode
        with open(write_file, "w") as write:
            # grab columns "first", "last", and "house"
            fieldnames = ["first", "last", "house"]
            # initialize csv.DictWriter on file
            writer = csv.DictWriter(write, fieldnames=fieldnames)
            # write csv header to output csv
            writer.writeheader()

            # take read file and output on write file
            # iterate over read file
            for row in reader:
                # destructure last, first names
                last, first = row["name"].split(",")
                house = row["house"]

                # write csv rows on write file
                writer.writerow({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": house
                })

if __name__ == "__main__":
    main()