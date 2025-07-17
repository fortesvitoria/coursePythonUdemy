import random

rock = "Rock! ✊"
paper = "Paper! ✋"
scissors = "Scissors! ✌"



#lopping
while True:
    try:
        # link the emoji to the pc choice
        choice_pc = random.randint(0, 2)
        choice_pc_index = 0
        ''''''
        if choice_pc == 0:
            choice_pc_index = rock
        elif choice_pc == 1:
            choice_pc_index = paper
        elif choice_pc == 2:
            choice_pc_index = scissors
        else:
            print('Invalid option!')
        choice_gamer = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: '))
        # link the emoji to the gamer choice
        choice_gamer_index = 0
        if choice_gamer == 0:
            choice_gamer_index = rock
        elif choice_gamer == 1:
            choice_gamer_index = paper
        elif choice_gamer == 2:
            choice_gamer_index = scissors
        else:
            print('Invalid option!')
        #empate
        if choice_pc == 0 and choice_gamer == 0 or choice_pc == 1 and choice_gamer == 1 or choice_pc == 2 and choice_gamer == 2:
            print(f'Your choice was: {choice_gamer,choice_gamer_index} and the computers choice was: {choice_pc,choice_pc_index}.')
            print('It\'s a draw! Try again!')

        #rock 0/paper 1 = paper wins
        elif choice_pc == 0 and choice_gamer == 1 or choice_pc == 1 and choice_gamer == 0:
            print(f'Your choice was: {choice_gamer, choice_gamer_index} and the computers choice was: {choice_pc, choice_pc_index}.')
            if choice_pc == 1:
                print('Sorry, you lost! =(')
            else:
                print('Congrats!!! You won!!!')

        #rock 0/scissors 2 = rock wins
        elif choice_pc == 0 and choice_gamer == 2 or choice_pc == 2 and choice_gamer == 0:
            print(f'Your choice was: {choice_gamer, choice_gamer_index} and the computers choice was: {choice_pc, choice_pc_index}.')
            if choice_pc == 0:
                print('Sorry, you lost! =(')
            else:
                print('Congrats!!! You won!!!')

        #paper 1/scissors 2 = scissors wins
        elif choice_pc == 2 and choice_gamer == 1 or choice_pc == 1 and choice_gamer == 2:
            print(f'Your choice was: {choice_gamer, choice_gamer_index} and the computers choice was: {choice_pc, choice_pc_index}.')
            if choice_pc == 2:
                print('Sorry, you lost! =(')
            else:
                print('Congrats!!! You won!!!')
        else:
            print('INVALID OPTION!')
    except:
        print('ERRO!')



