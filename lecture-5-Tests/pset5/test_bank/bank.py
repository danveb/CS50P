# Implement a Python program that promps user for a greeting
# if greeting starts with "hello", output $0
# if greeting starts with "h", output $20
# otherwise output $100

def main():
    # prompt user for input without any checks
    prompt = input("Greeting: ")
    print(value(prompt))

def value(greeting):
    # check for greeting in lowercase
    greeting = greeting.lower()
    # check if input starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # check if input starts with "h" at least
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()