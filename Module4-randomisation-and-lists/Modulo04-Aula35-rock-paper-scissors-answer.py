import random

rock = "Rock! ✊"
paper = "Paper! ✋"
scissors = "Scissors! ✌"

game_img = [rock, paper, scissors]

#user
choice_gamer = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: '))
if choice_gamer >= 0 or choice_gamer <= 2:
    print(game_img[choice_gamer])

#pc
choice_pc = random.randint(0, 2)
print(f'Computer choice {choice_pc} --- {game_img[choice_pc]}')

if choice_gamer >= 3 or choice_gamer < 0:
    print('Invalid choice!')
elif choice_gamer == 0 and choice_pc ==2:
    print('You win')
elif choice_pc == 0 and choice_gamer ==2:
    print('You lose!')
elif choice_gamer > choice_pc:
    print('You win!')
elif choice_pc > choice_gamer:
    print('You lose!')
elif choice_pc == choice_gamer:
    print('It\'s a draw!')
