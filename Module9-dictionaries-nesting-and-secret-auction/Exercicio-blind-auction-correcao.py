print('Welcome to the secret auction program.')

#cria dicionario
bidders = {}

choice_continue = True

#funcao comparativa com for
def winner_bidder (bidding_dictonary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictonary:
        bid_amount = bidding_dictonary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}. ')


#inicia programa com looping
while choice_continue:
    name = input('What\'s your name? ')
    bid = float(input('What\'s your bid? '))
    # adicionando nome e posta no dicionario
    bidders[name] = bid

    choice = input('Are there any other bidders? Type "yes " or "no". ')

    if choice.lower() == 'no':
        # após inserir no imprime a maior aposta e ganhador
        #encontra o maior lance
        choice_continue = False
        winner_bidder(bidders)

    elif choice.lower() == 'yes':
        print('\n'*20)

    elif choice.lower != 'yes':
        print('Type only "yes" or "no". ')



