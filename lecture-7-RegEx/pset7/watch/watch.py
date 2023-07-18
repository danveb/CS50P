# Implement a function called parse that expects a str of HTML as input
# extracts YouTube URL that’s the value of a src attribute of an iframe element therein
# returns its shareable youtu.be equivalent as a str.

# - expect that any such URL will be in one of the formats below
# - assume that the value of src will be surrounded by double quotes
# - assume that the input will contain no more than one such URL.
# if the input does not contain any such URL at all, return None.

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

import re
import sys

def main():
    # print(parse(input("HTML: ")))
    # prompt user for HTML
    prompt = input("HTML: ")
    # parse user input
    result = parse(prompt)
    print(result)

def parse(s):
    """Parse input URL and output pretty URL"""
    # pattern match with regex
    match = re.search(r'<iframe.*?src="([^"]*)"', s)
    if match:
        url = match.group(1)
        if 'youtube.com' in url or 'youtu.be' in url:
            video_id = re.search(r'/embed/([^\?]+)', url).group(1)
            return f'https://youtu.be/{video_id}'
    return None

if __name__ == "__main__":
    main()