from random import randint

logo = """
  _____                   _  __           __           _             _____              
 / ___/_ _____ ___ ___   / |/ /_ ____ _  / /  ___ ____(_)__  ___ _  / ___/__ ___ _  ___ 
/ (_ / // / -_|_-<(_-<  /    / // /  ' \/ _ \/ -_) __/ / _ \/ _ `/ / (_ / _ `/  ' \/ -_)
\___/\_,_/\__/___/___/ /_/|_/\_,_/_/_/_/_.__/\__/_/ /_/_//_/\_, /  \___/\_,_/_/_/_/\__/ 
                                                           /___/                        
"""

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
turn = 0

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("To low")
        return turns - 1
    else:
        print("You got it! The answer was")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    global turn
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        turn = check_answer(guess, answer, turns)
        print(turn)
        if turn == 0:
            print(f"You've run out of guess, you lose")
        elif guess != answer:
            print("Guess again.")

print(logo)
game()