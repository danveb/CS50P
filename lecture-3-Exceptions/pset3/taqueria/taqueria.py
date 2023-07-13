# Implement a program that enables a user to place an order
# prompt user for an item, one per line until user inputs "control-d"
# after each item is inputted, display total cost of all items so far, prefixed with $ and two decimals

# how to iterate through a dictionary?
# selection = "Bowl"
# for item in menu:
#     if selection in item:
#         print(menu[selection]) # 8.5

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    # initialize total as 0
    total = 0
    while True:
        try:
            # prompt user for a menu item
            item = input("Item: ").title()
            # check: if item is in menu
            if item in menu:
                # calculate_total with current item
                total += menu[item]
                # print its total value
                print(f"Total: ${total:.2f}")
        except (EOFError, KeyError):
            print("\n")
            break

main()
