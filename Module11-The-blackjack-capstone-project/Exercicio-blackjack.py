import random

def deal_card():
    # returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    #a blackjack only happens when we have a hand with only two cards (11,10)
    #1º option:
    #if 11 in cards and 10 in cards and len(cards) == 2:
    #2º option
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #zero score of blackjack
    
    #inside calculate_score we should also check for a 11(ace), if the score is already over 21, remove the 11 and replace with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    #function sum and calculate numbers inside a list
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw!"
    elif c_score == 0:
        return "Lose, computer has Blackjack!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You went over 21. You lose!"
    elif c_score > 21:
        return "Computer went over 21. You win!"
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    game_over = False


    for _ in range(2):    
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}.")
        print(f"Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else: 
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: \n")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play another game? Type 'y' or 'n': \n") == "y":
    play_game()