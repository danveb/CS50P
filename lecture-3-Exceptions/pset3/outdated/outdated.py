# Implement a Python program that prompts user for a date in month-day-year order
# output the same date in "YYYY-MM-DD" format
# if the input is NOT valid in either format we prompt user again

# Date: 9/8/1636
# 1636-09-08

# Date: September 8, 1636
# 1636-09-08

def main():
    # initialize months []
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    # keep looping while True
    while True:
        # try/except block
        try:
            # prompt user for a Date in month-day-year format; remove whitespaces
            prompt = input("Date: ").strip()
            # check: if current input has " "
            if " " in prompt:
                # split month, day, year at " "
                month, day, year = prompt.split(" ")
                if month.title() in months:
                    day = int(day.strip(","))
                    month = int(months.index(month)) + 1
                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break
            # check: if current input does NOT contain spaces
            elif not " " in prompt:
                month, day, year = map(int, prompt.split("/"))
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

        except ValueError:
            continue
        except (EOFError, KeyboardInterrupt):
            print("", end="\n")
            quit()
        else:
            continue

main()