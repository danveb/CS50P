# Implement a Python program that expects 2 command-line arguments -> len(sys.argv) == 3
# - sys.argv[1] -> name of JPEG or PNG to read (open) as input
# - sys.argv[2] -> name of JPEG or PNG to write (save) as output

# the program exits by system:
# - if user does not specify 2 command-line arguments
# - if input/output names do not end in ".jpg", ".jpeg", or ".png", case-insensitive
# - if input name does not have SAME extension as output name
# - if specified input file does NOT exist

import sys
import os
from PIL import Image, ImageOps

def main():
    # check: if command-line arguments are less than 2
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # check: if command-line arguments are more than 2
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        # initialize read,write files from command-line arguments
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        input_file_ext = sys.argv[1].split(".")[1]
        output_file_ext = sys.argv[2].split(".")[1]

        # initialize allowed_extensions []
        allowed_extensions = ["jpeg", "jpg", "png", "JPEG", "JPG", "PNG"]

        # check: if input/output file ext not in allowed_extensions []
        if input_file_ext not in allowed_extensions:
            sys.exit("Invalid output")
        elif output_file_ext not in allowed_extensions:
            sys.exit("Invalid output")
        # check: if extensions do NOT match
        elif input_file_ext != output_file_ext:
            sys.exit("Input and output have different extensions")
        # check: if input file does NOT exist
        elif not os.path.isfile(input_file):
            sys.exit("Input does not exist")
        else:
            # DO SOMETHING
            print_shirt(input_file, output_file)

def print_shirt(input_file, output_file):
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    # fit to resive and crop image
    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))

    photo.paste(shirt, shirt)
    photo.save(output_file)

if __name__ == "__main__":
    main()