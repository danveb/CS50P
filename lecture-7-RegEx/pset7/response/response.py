# Implement a Python program that prompts the user for an email address via "input"
# print "Valid" or "Invalid" based on a syntactically valid email address
# - use validator-collection or validators from PyPI

import validators

def main():
    # prompt user to type in an email address
    prompt = input("What's your email address? ")
    # validate the email address with helper function
    print(validate_email(prompt))

def validate_email(address):
    """Validate an email address"""
    output = validators.email(address)
    if output:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
