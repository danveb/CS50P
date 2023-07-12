# Implement a Python program to build a tip calculator

def main():
    """Calculates tip conversion"""
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """Calculate dollars to float point number"""
    # accept a "str" as input, remove leading $ and return amount as float
    # replace $ and leave empty
    dollar_str = d.replace("$", "")
    # return as float
    return float(dollar_str)

def percent_to_float(p):
    """Calculate percentage to float point number"""
    # accept a "str" as input, remove trailing % and return amount as float
    # replace % and leave empty
    percent_str = p.replace("%", "")
    # return as float; make sure to divide by 100
    return float(percent_str)/100

main()
