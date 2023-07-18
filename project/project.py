# Python meme generator that outputs a .jpg file

from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys


def main():
    """Funny Meme Generator with sample Image"""
    # prompt user for a top text/bottom text
    top_text = input("Top text: ").strip()
    bottom_text = input("Bottom text: ").strip()
    # submit both texts for length correctness
    top_text = check_length(top_text)
    bottom_text = check_length(bottom_text)
    # submit both texts for text correctness
    clean_top_text = check_capitalize(top_text)
    clean_bottom_text = check_capitalize(bottom_text)

    # start building the meme
    return memefy(clean_top_text, clean_bottom_text)


def check_length(text):
    """Checks text for min/max length of characters"""
    # initialize limit at 40 characters
    char_max_threshold = 40
    # initialize min_threshold at 5
    char_min_threshold = 5
    # check: if length of characters passes limit we'll throw an error and exit
    if len(text) > char_max_threshold:
        sys.exit("Over 40 characters... please consider shortening it")
    # check: if length of characters is below the min_threshold we'll throw an error and exit
    elif len(text) < char_min_threshold:
        sys.exit("Minimum 5 characters...")
    # if OK we'll return the text
    return text


def check_capitalize(text):
    """Returns capitalized text"""
    # initialize new_str as ""
    new_str = ""
    # iterate over each character in text
    for character in text:
        new_str += character.upper()
    return new_str


def memefy(top_text, bottom_text):
    """Build the meme as .jpg format"""
    # load the base image template
    base_image = Image.open("harold-meme.jpg")

    # instantiate ImageDraw.Draw class on base_image
    draw = ImageDraw.Draw(base_image)

    # use font and set text size
    font = ImageFont.truetype("impact.ttf", 30)

    # calculate text positions (trial and error to get to specific position)
    top_text_position = (base_image.width // 2, 250)
    bottom_text_position = (base_image.width // 2, base_image.height - 50)

    # set font and border colors (white/black for contrast)
    text_color = (255, 255, 255)
    border_color = (0, 0, 0)

    # set border size
    border_size = 2

    # wrap top/bottom text to fit within the width of image
    top_text_wrapped = textwrap.wrap(top_text, width=35)
    bottom_text_wrapped = textwrap.wrap(bottom_text, width=35)

    # draw the border text for top text
    for dx in range(-border_size, border_size + 1):
        for dy in range(-border_size, border_size + 1):
            draw.text((top_text_position[0] + dx, top_text_position[1] + dy), '\n'.join(top_text_wrapped), fill=border_color, font=font, anchor="ms")

    # draw the main top text
    draw.text(top_text_position, '\n'.join(top_text_wrapped), fill=text_color, font=font, anchor="ms")

    # draw the border text for bottom text
    for dx in range(-border_size, border_size + 1):
        for dy in range(-border_size, border_size + 1):
            draw.text((bottom_text_position[0] + dx, bottom_text_position[1] + dy), '\n'.join(bottom_text_wrapped), fill=border_color, font=font, anchor="ms")

    # draw the main bottom text
    draw.text(bottom_text_position, '\n'.join(bottom_text_wrapped), fill=text_color, font=font, anchor="ms")

    # save image as meme.jpg
    base_image.save("meme.jpg")

    # return the image
    return "meme.jpg"


if __name__ == "__main__":
    main()

