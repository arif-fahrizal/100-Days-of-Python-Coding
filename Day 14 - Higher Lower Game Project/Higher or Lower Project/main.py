from random import choice
from art import logo, vs
from game_data import data

# Format Data
def format_data(account):
    """Takes the account data and returns the printable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(user_guess, followers_a, followers_b):
    """Take a user's guess and the follower counts and returns if they got it right."""

    if followers_a > followers_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
should_continue = True
data_b = choice(data)

while should_continue:
    # Generate Random Account from data
    data_a = data_b
    data_b = choice(data)

    if data_a == data_b:
        data_b = choice(data)

    print(f"Compare A: {format_data(data_a)}")
    print(vs)
    print(f"Against B: {format_data(data_b)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    guessed = ""
    if guess == 'a':
        guessed = data_a
    elif guess == 'b':
        guessed = data_b
    else:
        print("Invalid input. Please type 'A' or 'B'.")
        continue

    if guessed['follower_count'] == max(data_a['follower_count'], data_b['follower_count']):
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        should_continue = False


    # Check if user is correct
    # - Get follower count of each account
    # followers_a = data_a['follower_count']
    # followers_b = data_b['follower_count']

    # is_correct = check_answer(guess, followers_a, followers_b)
    #
    # if is_correct:
    #     score += 1
    #     print(f"You're right! Current score: {score}.")
    # else:
    #     print(f"Sorry, that's wrong. Final score: {score}.")
    #     should_continue = False
