# Implement a Python program that prompts user to insert a coin (integer only)
# once user inputs at least 50 cents, output the change the user is owed
# ignore any integer that isn't an accepted denomination
# machine only accepts 25, 10, and 5 cents

def main():
    # initialize cost as 50 by default
    cost = 50
    # initialize available as 0 by default
    available = 0
    # initialize valid_coins as []
    valid_coins = [25, 10, 5]

    # keep looping while available < 50
    while available < cost:
        # print amount due as cost - available
        print(f"Amount Due: {cost - available}")
        # prompt user to insert a coin (25, 10, 5 as integer)
        coin = int(input("Insert Coin: "))
        if coin in valid_coins:
            available += coin
        else:
            continue

    # print "Change Owed"
    print(f"Change Owed: {available - cost}")

main()