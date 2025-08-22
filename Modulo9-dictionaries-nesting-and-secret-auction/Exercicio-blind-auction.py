print('Welcome to the secret auction program.')

#cria dicionario
bidders = {}

#cria funcao para achar o maior
def maior_lance(lance):
    # encontra o maior lance
    winner = max(lance, key=bidders.get)  # usa metodo max para pegar o maior valor e metodo get para acessar
    maior = lance[winner]

    print(f'The winner is {winner} with a bid of ${maior}.')

#inicia programa com looping
while True:
    name = input('What\'s your name? ')
    bid = float(input('What\'s your bid? '))
    choice = input('Are there any other bidders? Type "yes " or "no". ')
    # adicionando nome e posta no dicionario
    bidders[name] = bid

    # após limpa a tela e pede nome novamente
    print('\n' * 100)

    if choice.lower() == "no":
        # após inserir no imprime a maior aposta e ganhador com funcao
        maior_lance(bidders)
        break

    elif choice.lower != 'yes':
        print('Type only "yes" or "no". ')