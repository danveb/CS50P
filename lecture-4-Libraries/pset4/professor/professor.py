# Implement a Python program:
# - prompt user for a level "n". if user does not input 1, 2, 3 the program prompts again
# - randomly generate 10 math problems formatted as X + Y =
# - prompt user to solve each of those problems. if answer is NOT correct, program outputs EEE and prompts user again up to 3 tries; if user fails to answer after 3 tries program outputs correct answer
# - program should output the user's score: number of correct answers out of 10

# per tests:
# level 1 -> 0-9
# level 2 -> 10 - 99
# level 3 -> 100 - 999

from random import randint
import sys

def main():
    """Play Professor"""
    # initialize score, strike at 0
    score = 0
    strike = 1

    # initialize play_level
    play_level = get_level()

    # initialize 10 games
    # generate integers for x, y
    # math_problem formatted as X + Y =
    for _ in range(10):
        x = generate_integer(play_level)
        y = generate_integer(play_level)
        answer = x + y
        math_problem = int(input(f"{x} + {y} = "))

        if math_problem == answer:
            score += 1

        while math_problem != answer:
            # increase strike by 1 and print "EEE"
            strike += 1
            print("EEE")
            # reprompt same math problem
            math_problem = int(input(f"{x} + {y} = "))
            # check: if 3 strikes? we'll print the answer and exit with score
            if strike >= 3:
                print(f"{x} + {y} = {answer}")
                sys.exit(f"Score: {score}")

    # after 10 problems we'll print the score
    print(f"Score: {score}")

def get_level():
    """Prompts user for a level between 1, 2 and 3"""
    # prompt user for a level between 1, 2 and 3
    level = input("Level: ")
    # check:
    if level.isalpha() or int(level) <= 0 or int(level) > 3:
        input("Level: ")
    else:
        level = int(level)
        for i in [1, 2, 3]:
            if level == i:
                return level

def generate_integer(level):
    """Returns a randomly generated non-negative integer"""
    try:
        # check: if level 1
        if level == 1:
            # generate random int between 0-9
            random_int = randint(0, 9)
            # print(random_int)
            return random_int
        # check: if level 2
        elif level == 2:
            # generate random int between 10-99
            random_int = randint(10, 99)
            # print(random_int)
            return random_int
        # check: if level 3
        elif level == 3:
            # generate random int between 100-999
            random_int = randint(100, 999)
            # print(random_int)
            return random_int
    except:
        raise ValueError

if __name__ == "__main__":
    main()

# test
# get_level() # 2
# generate_integer(1) # 5
# generate_integer(2) # 74
# generate_integer(3) # 837