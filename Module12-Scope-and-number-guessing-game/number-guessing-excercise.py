'''
easy - 10 attempts
hard - 5 attempts

'''
import random
random_number = random.randint(1,100)
print(random_number)
print("Welcome to the guessing game!")
print("I'm thinking a number from 1 to 100.")

#user choose the difficulty
while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if choice == 'easy':
        choice_number = 10
        print("You have 10 attempts!")
        break
    elif choice == 'hard':
        choice_number = 5
        print("You have 5 attempts!")
        break
    else:
        print("Invalid choice")

#loop that receives the number of choice attemps and breaks when the guess is right
for i in range(choice_number):
    user_guess = int(input(f"You have {choice_number} attempts left. Guess a number:"))
    choice_number -=1
    if user_guess == random_number:
        print ("You win.")
        break
    else:
        print("Wrong guess! Try again")
else:
    print(f"Sorry, you lost! the correct number is {random_number}")