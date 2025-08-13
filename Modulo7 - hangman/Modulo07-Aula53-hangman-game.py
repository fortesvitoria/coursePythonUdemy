#importa random
import random

#importa listas
from Modulo07_lista_hangman import word_list
from Modulo07_hangman_stages import stages

#gera palavra aleatoria através do index
index = random.randint(0, len(word_list) -1)

#aguarda nome do alimento pelo index
palavra = word_list[index] #pega a palavra da lista
palavra_lista = list(palavra) #transforma a palavra em uma lista

#contagem letras
soma = len(palavra)

#contagem vidas
lives = 6

#gera espaços e guarda na variavel
espacos = ['_' for _ in palavra]

print('Welcome to the HANGMAN GAME! You got 6 lives!')
print(f'Word to guess {'_' * len(palavra)}, {palavra}')

while True:
    try:
        guess = input('Guess a letter: ')

        if guess in palavra and soma > 0:
            for i in range(len(palavra_lista)):
                if palavra_lista[i] == guess and espacos[i] == '_': #se a palavra na lista for igual a guess e os espaços estiverem vazios, adiciona a letra
                    espacos[i] = guess
                    soma -= 1 #contagem
            print(f'{espacos}')
        elif guess not in palavra:
            lives -= 1 #se o chute nao estiver na palavra, perde uma vida
            print(f'The letter {guess} in not in the word.')
            print(f'You got {lives} lives!')
            if lives == 0:
                print('GAME OVER!')
                break
        if soma == 0: #finaliza
            print('CONGRATULATIONS! YOU WON!')
            break
    except:
        print('ble')