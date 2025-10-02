#importa random
import random

#importa listas
from Modulo07_lista_hangman import word_list
from Modulo07_hangman_stages import stages

#contagem de vidas
lives = 6

#Generate a random word
choice = random.choice(word_list)
print(choice)


#cria placeholder com a mesma quantidade de números da palavra escolhida
placeholder = ''
word_len = len(choice)
for position in range(word_len):
    placeholder += '_'
print(placeholder)

game_over = False

#cria lista
correct_letters = []

#looping
while not game_over:
    #Ask for a letter
    print(f'{5 * '*', 'You got', lives}/6 lives  {5 * '*'}')
    guess = input("Guess a letter: ").lower()
    print(guess)


    # avisa se a palavra esta repetida
    if guess in correct_letters:
        print(f'You already guessed {guess}')

    display = ''

    for letter in choice: #verifica se a letra esta na palavra escolhida
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    if guess not in choice:
        lives -= 1
        print(f'You guesses {guess}. The letter is not in the word. You lose a life.')
        if lives == 0:
            game_over = True
            print('You lose =( GAME OVER')
            print(f'The corred word is {choice}')

    print(stages[lives])

    print(display)
    if '_' not in display:
        game_over = True
        print('You win!')
