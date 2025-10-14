'''
easy - 10 attempts
hard - 5 attempts

'''
import random

#choosing a number from 1 to 100
random_number = random.randint(1,100)
print(random_number)
print("Welcome to the guessing game!")
print("I'm thinking of a number from 1 to 100.")

hard_level = 5
easy_level = 10

#user choose the difficulty
def set_dificulty():
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
        if choice == 'easy':
            return easy_level
        elif choice == 'hard':
            return hard_level
        else:
            print("Invalid choice")

#letting the user guess a number
#loop that receives the number of choice attemps and breaks when the guess is right
def check_answer(user_guess, random_number, turns):
    if user_guess < random_number:
        print('Too low. Try again!')
        return turns - 1
    elif user_guess > random_number:
        print('Too high. Try again!')
        return turns - 1
    else:
        print (f"You win. The number was {random_number}!")

#starting game
def game():
    turns = set_dificulty()
    user_guess = 0
    while user_guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(user_guess, random_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != random_number:
            print("Guess again.")

game()
