# Implement a Python program that prompts user for their date of birth in YYYY-MM-DD format
# print out how old they are in minutes, rounded to nearest integer
# assume user was born at midnight (00:00:00), and assume current time is also midnight
# - if user does NOT input a date in YYYY-MM-DD format we'll exit system with error message

# Date of Birth: January 1, 1999
# Invalid Date

# Date of Birth: 1999-01-01
# Five hundred twenty-five thousand, six hundred minutes

# Date of Birth: 1999-12-31
# One thousand, four hundred forty minutes

# Date of Birth: 1970-01-01
# Fifteen million, seven hundred seventy-eight thousand eighty minutes

from datetime import date
import sys
import inflect
p = inflect.engine()

def main():
    # prompt user for a date of birth
    birthdate = input("Date of Birth: ")
    # check for valid_date on birth_date
    valid_date = validate_birthdate(birthdate)
    days_difference = calculate_difference(valid_date)
    output = add_text(days_difference)
    print(output)

def validate_birthdate(birthdate):
    try:
        input = date.fromisoformat(birthdate)
        # print(input)
        return input
    except ValueError:
        sys.exit("Invalid date")

def calculate_difference(days):
    today = date.today()
    days_difference = today - days
    days_difference.days * 24 * 60
    return days_difference.days * 24 * 60

def add_text(text):
    text = p.number_to_words(text, andword="")
    return text.capitalize() + " minutes"

if __name__ == "__main__":
    main()