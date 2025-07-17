RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
BLUE = "\033[94m"
WHITE = "\033[97m"
RED = "\033[91m"
BG_BLUE = "\033[44m"
SETA = "\u2794"

print(f'{BOLD}{BLUE}Welcome to the Treasure Island!')
print(f'{BOLD}{BLUE}Your mission is to find the treasure.')
option = input(f'{BOLD}{BLUE}You\'re at a cross road. Where do you want to go? Right or Left? {RESET}').upper()

if option.upper() == 'RIGHT':
    print(f'{BOLD}{RED}YOU FELL INTO A HOLE!!! GAME OVER!!!{RESET}')
elif option == 'LEFT':
    option = input(f'{BOLD}{BLUE}You\'ve come to a lake. '
                   f'There is an island in the middle of the lake.'
                   f'Do you choose to swim  to the land or wait for a boat? {RESET}').upper()
    if option == 'SWIM':
        print(f'{BOLD}{RED}YOU GOT ATTACKED BY AND HUNGRY SHARK!!! GAME OVER!!!{RESET}')
    elif option == 'WAIT':
        option = input(f'{BOLD}{BLUE}You arrive at the island unharmed.'
                       f'There is a house with 3 doors. '
                       f'One BLUE,one RED and one YELLOW.'
                       f'Which one do you choose? {RESET}').upper()
        if option == 'BLUE':
            print(f'{BOLD}{RED}IT\'S A ROOM FULL OF FIRE!!! GAME OVER!!!{RESET}')
        elif option == 'RED':
            print(f'{BOLD}{RED}YOU ENTER A ROOM OF BEASTS!!! GAME OVER!!!{RESET}')
        elif option == 'GREEN':
            print(f'{BOLD}{GREEN}!! CONGRATS, YOU WIN!!!{RESET}')
        else:
            print(f'{BOLD}{RED}Invalid option!')
    else:
        print(f'{BOLD}{RED}Invalid option!')
else:
    print(f'{BOLD}{RED}Invalid option!')

