import random
import game_data

def get_random():
    #gets a random instagram account from game_data and return the values
    return random.choice(game_data.data)

def format_account(account):
    #gets the values from the account and return a string
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a" # Will be True if guess is 'a', False otherwise
    else:
        return guess == "b" # Will be True if guess is 'b', False otherwise
    
def game():
    score = 0
    game_over = False

    #get two random accounts
    account_a = get_random()
    account_b = get_random()

    #make sure two accounts re not the same
    while account_a == account_b:
        account_b = get_random()

    #starting the main looping
    while not game_over:
        # re-use the winner from the previous round
        # on the first turn, this is just the initial random account
        account_a = account_a
        account_b = get_random()
        print(f"Compare A: {format_account(account_a)}.")
        print("VS")
        print(f"Against B: {format_account(account_b)}.")

        # Get follower counts
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        guess = ""
        while guess not in ("a","b"):
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print("You win!")
        else:
            game_over = True
            print(f"\nSorry, that's wrong.")
            print(f"{account_a['name']} has {a_follower_count} million followers.")
            print(f"{account_b['name']} has {b_follower_count} million followers.")
            print(f"Your final score is: {score}")

game()
