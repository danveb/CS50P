# Implement a Python program that promps user for a greeting
# if greeting starts with "hello", output $0
# if greeting starts with "h", output $20
# otherwise output $100

def main():
    """Greets customer"""
    # greet user for input
    user_input = input("Greeting: ").strip().lower()
    # check: if user_input starts with "hello" print $0
    if user_input.startswith("hello"):
        print("$0")
    # check: if user_input starts with "h" but NOT "hello" print $20
    elif user_input.startswith("h"):
        print("$20")
    # else print $100
    else:
        print("$100")

main()