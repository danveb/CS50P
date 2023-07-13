# Implement a Python program that promps user for items
# output user's grocery list in all uppercase, sorted alphabetically by item, prefix with number of times input

# Intuition
# - prompt user to input grocery list items
# - if current element NOT in grocery list we'll add 1
# - if current element IS in grocery list we'll update its count by 1 more

grocery_list = [
    {
        "item": "apple",
        "quantity": 1,
    },
    {
        "item": "banana",
        "quantity": 2,
    },
    {
        "item": "ice cream",
        "quantity": 1,
    },
]

# my_item = "apple"
# for item in grocery_list:
#     print(item["item"]) # apple, banana, ice cream
#     print(item["quantity"]) # 1, 2, 1

def main():
    # initialize a grocery_list []
    grocery_list = []
    # initialize count {}
    count = {}

    # keep looping while True
    while True:
        try:
            # prompt user to enter a grocery item in uppercase
            prompt = input("").upper()
            # add grocery item to grocery_list and sort it automatically
            grocery_list.append(prompt)
            grocery_list.sort()
        except (EOFError, KeyError):
            for item in grocery_list:
                if item in count:
                    count[item] += 1
                else:
                    count[item] = 1
            for x in count:
                print(str(count[x]) + " " + x)
            break
        else:
            continue

main()