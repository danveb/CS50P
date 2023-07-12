# Implement a Python program that prompts a user for a vanity plate
# output "Valid" if it meets all requirements
# output "Invalid" if it does not
# any letters in user's input are uppercase

# Vanity plates must start with at least 2 letters
# maximum of 6 characters (letters or numbers) and minimum of 2 characters
# numbers are not allowed in middle of a plate; must be at end; first number can't be a 0
# - AAAA222, AAA22A are NOT acceptable
# no periods, spaces or punctuation marks are allowed

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # get length of string
    length = len(s)

    # check: if length is >= 2 and <= 6
    if length >= 2 and length <= 6:
        for characters in s:
            # if not alphanumeric we can break
            if not s.isalnum():
                break
            # first 2 characters are letters
            if s[0:2].isalpha():
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

            zeroIdx = s.find("0") - 1

            if s[-(zeroIdx)].isdigit():
                for x in s:
                    if x.isdigit():
                        if x.startswith("0"):
                            return False
                        else:
                            return True

            if s[-2].isdigit() and s[-1].isalpha():
                break
            elif s[-2].isdigit():
                return True
            elif s.isalpha():
                return True
    else:
        return False

main()