import random

rock = "Rock! ✊"
paper = "Paper! ✋"
scissors = "Scissors! ✌"

#lopping
while True:
    try:
        game_img = [rock, paper, scissors]

        # user
        choice_gamer = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: '))

        # pc
        choice_pc = random.randint(0, 2)
        print(f'Computer choice {choice_pc} --- {game_img[choice_pc]}')

        #condicionais
        if choice_gamer >= 3 or choice_gamer < 0:
            print(f'Invalid choice! You chose {game_img[choice_gamer]}' )
        elif choice_gamer == 0 and choice_pc == 2:
            print(f'Your choice was: {choice_gamer, game_img[choice_gamer]} and the computers choice was: {choice_pc, game_img[choice_gamer]}.')
            print('You win')
        elif choice_pc == 0 and choice_gamer == 2:
            print(f'Your choice was: {choice_gamer, game_img[choice_gamer]} and the computers choice was: {choice_pc, game_img[choice_gamer]}.')
            print('You lose!')
        elif choice_gamer > choice_pc:
            print(f'Your choice was: {choice_gamer, game_img[choice_gamer]} and the computers choice was: {choice_pc, game_img[choice_gamer]}.')
            print('You win!')
        elif choice_pc > choice_gamer:
            print(f'Your choice was: {choice_gamer, game_img[choice_gamer]} and the computers choice was: {choice_pc, game_img[choice_gamer]}.')
            print('You lose!')
        elif choice_pc == choice_gamer:
            print(f'Your choice was: {choice_gamer, game_img[choice_gamer]} and the computers choice was: {choice_pc, game_img[choice_gamer]}.')
            print('It\'s a draw! Try again!')
    except:
        print('ERRO! OPÇÃO INVALIDA!')




