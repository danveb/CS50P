# Implement a Python program that promps user for a time
# output whether "breakfast time", "lunch time", "dinner time"
# assume user's input is formatted in 24-hour time

def main():
    """Main function to calculate meal time"""
    # prompt user for a time
    user_input = input("What time is it?? ")
    # check: if input has "." we continue
    if "." in user_input:
        time = user_input
    # check: if input has ":" convert
    else:
        time = convert(user_input)

    # check: if between 7:00 and 8:00 -> breakfast
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    # check: if between 12:00 and 13:00 -> lunch
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    # check: if between 18:00 and 19:00 -> dinner
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

def convert(time):
    """Convert input time as float"""
    hours, minutes = time.split(":")
    t = float(hours) + (float(minutes) / 60)
    return t

if __name__ == "__main__":
    main()
