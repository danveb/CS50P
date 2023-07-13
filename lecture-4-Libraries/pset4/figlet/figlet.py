# Implement a Python program that expects 0 or 2 command-line arguments
# 0 if user would like to output text in a random font
# 2 if user would like to output text in a specific font "--font", name of font
# prompt user to input a "str" of text
# output text in desired font
# check: if user provides 2 arguments and the first is not "--font" or second is not name of font we exit "sys.exit("Error...")"

import sys
from pyfiglet import Figlet
from random import choice

def main():
    # initialize figlet
    figlet = Figlet()
    # initialize available fonts
    available_fonts = figlet.getFonts()

    # check: if 0 command-line arguments? output text in random font
    if len(sys.argv) == 1:
        # prompt user to input a "str" of text
        prompt = input("Input: ").strip()
        # generate and save a random font
        random_font = get_random_font()
        # set Figlet font
        figlet.setFont(font=random_font)
        # output text in random font
        print(f"Output: {figlet.renderText(prompt)}")

    # check: if 2 command-line arguments? require "--font", name of font
    elif len(sys.argv) == 3:
        # check that 1st argument does NOT include "--font" or "-f"
        # check that 2nd argument is NOT name of font
        if not str(sys.argv[1]) in ["--font", "-f"] or not str(sys.argv[2]) in available_fonts:
            # we exit the system with a message
            sys.exit("Error found... please try again")
        # else we perform all the code
        else:
            # prompt user to input a "str" of text
            prompt = input("Input: ").strip()
            # set Figlet font with our choice of font on argv[2]
            figlet.setFont(font=sys.argv[2])
            # output text
            print(f"Output: {figlet.renderText(prompt)}")

    # check: system exit
    else:
        sys.exit("Sorry, error found...")

def get_random_font():
    """Get a random font from Figlet"""
    # initialize figlet
    figlet = Figlet()
    available_fonts = figlet.getFonts()
    random_font = choice(available_fonts)
    return random_font

main()
get_random_font() # cosmic, morse, xsbookb, etc.