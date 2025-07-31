
#importa random
import random

#Generate a random word
alimentos = ['leite', 'couve', 'arroz', 'feijao', 'banana', 'cenoura', 'pão', 'tomate', 'ovo', 'maionese']

#gera palavra aleatoria através do index
index = random.randint(0, len(alimentos) -1)

#aguarda nome do alimento pelo index
palavra = alimentos[index] #pega a palavra da lista
palavra_lista = list(palavra) #transforma a palavra em uma lista

soma = len(palavra)

#gera espaços e guarda na variavel
espacos = ['_' for _ in palavra]


print(f'Word to guess {'_' * len(palavra)}, {palavra}')

while True:
    try:
        guess = input('Guess a letter: ')
        index_guess = palavra_lista.index(guess) #descobre o index da letra na lista

        if guess in palavra and soma > 0:
            for i in range(len(palavra_lista)):
                if palavra_lista[i] == guess and espacos[i] == '_': #se a palavra na lista for igual a guess e os espaços estiverem vazios, adiciona a letra
                    espacos[i] = guess
                    soma -= 1 #contagem
            print(f'{espacos}')
        if soma == 0: #finaliza
            print('CONGRATULATIONS! YOU WON!')
            break
        else:
            print('beeeeh')
    except:
        print('invalido')




