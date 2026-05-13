from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)
print(answer)

EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too High.")
    elif user_guess < actual_answer:
        print("Too Low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

# Function tu set difficulty
def set_difficulty():
    choice_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if choice_level == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

turns = set_difficulty()

while turns > 0:
    # Let the user guess a number
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    check_answer(guess, answer)
    if guess == answer:
        break

    turns -= 1

if turns == 0:
    print("You've run out of guesses. You lose!")
    print(f"The correct answer was {answer}.")