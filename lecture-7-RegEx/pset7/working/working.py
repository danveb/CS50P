# Implement a Python program that expects a "str" in either 12-hour format
# return a corresponding 24-hour format
# expect AM and PM will be capitalized (with no periods therein) and there will be a space before each
# assume these times are representative of actual times
# raise a ValueError if input to convert is not either of those formats or if time is invalid

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # pattern match
    is_correct_format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    # check if is_correct_format
    if is_correct_format:
        # set pieces as a group ('9:00', '9', '00', 'AM', '5:00', '5', '00', 'PM')
        pieces = is_correct_format.groups()
        # check: if any piece above 12?
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        # format hour, minute, am/pm
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    # check if am or pm
    if am_pm == "PM":
        if int(hour) == 12:
            # convert to 12
            new_hour = 12
        else:
            # add 12 to hour
            new_hour = int(hour) + 12
    # else hour remains as PM
    else:
        if int(hour) == 12:
            # convert hour to 0
            new_hour = 0
        else:
            new_hour = int(hour)

    # check minutes
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
        # print(new_time)
    else:
        new_time = f"{new_hour:02}" + ":" + minute
        # print(new_time)
    return new_time

if __name__ == "__main__":
    main()