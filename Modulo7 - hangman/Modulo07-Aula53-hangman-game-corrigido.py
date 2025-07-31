#importa random
import random

#lista de imagens 6
stages = ['''
  +---+
  |   |
  0   |
 /|/  |
 / |  |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|/  |
 /    |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|/  |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
  |   |
      |
      |
=======
''','''
  +---+
  |   |
  0   |
      |
      |
      |
=======
''','''
  +---+
  |   |
      |
      |
      |
      |
=======
''']

#contagem de vidas
lives = 6

#Cria lista
word_list = ['leite', 'couve', 'arroz', 'feijao', 'banana', 'cenoura', 'pão', 'tomate', 'ovo', 'maionese']

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
    guess = input("Guess a letter: ").lower()
    print(guess)

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
        if lives == 0:
            game_over = True
            print('You lose =( GAME OVER')

    print(stages[lives])

    print(display)
    if '_' not in display:
        game_over = True
        print('You win!')
