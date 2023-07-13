# Implement a Python program where:
# prompt user for a level "n"; if user does not input a positive integer, program reprompts
# randomly generate an integer between 1 and "n", inclusive
# prompts user to guess the integer
# if guess is NOT positive integer, prompt user again for guess
# if guess is < integer output "Too small!" and prompt again
# if guess is > integer output "Too large!" and prompt again
# if guess == integer, output "Just right!" and exit

from random import randint

def main():
    while True:
        try:
            # prompt user for a level "n"
            level = int(input("Level: "))
            # # check: if level is positive integer
            if level >= 1:
                # generate a random num between 1 and "n" inclusive
                random_num = generate_random_num(level)
                # play guessing game with random num
                play_game(random_num)
                break
        except (TypeError, ValueError):
            continue

def generate_random_num(x):
    """Generate a random num as int"""
    # generate a random number between range 1 to x inclusive
    random_num = randint(1, x)
    return random_num

def play_game(num):
    while True:
        # prompt user to guess an integer
        guess = int(input("Guess: "))
        try:
            # check: if guess < num print "Too small!" and reprompt
            if guess < num:
                print("Too small!")
            # check: if guess > num print "Too large!" and reprompt
            elif guess > num:
                print("Too large!")
            # check: if guess == num print "Just right!" and exit
            else:
                print("Too large!")
                break
        except (TypeError, ValueError):
            continue

if __name__ == "__main__":
    main()