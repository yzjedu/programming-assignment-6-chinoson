# Henderson Fryer
# CS701_W02
# Submitted 08/24/2024

import random

# Function that generates a shuffled deck of 52 cards.
# Function that returns the name of a card given its string representation.
# Function that displays the names of the cards in a hand.
# Function that calculates and returns the total value of a hand.

def main():
    # Write the code for the main function here and delete pass

    # Welcome user and confirm continuation of game
    userIn = input("Welcome to automated blackjack! Enter '1' to start or 'q' to quit: ")
    
    # If user wants to play, proceed
    if userIn == '1':

    
        # Create full, shuffled deck
        deck = generate_deck()

        # Initialize empty hands for player and dealer
        dealerHand = []
        playerHand = []

        #draw two cards for each hand to start the game
        dealerHand.extend(deck[0:2])
        del deck[0:2]
        playerHand.extend(deck[0:2])
        del deck[0:2]

        # Provide hand info to player
        print("Your hand is: ", end='')
        display_hand(playerHand)
        print("With a value of: ", end = '')
        print(hand_value(playerHand))

        # Let user decide if they want to hit
        hit = input("Would you like to hit? Press 'y' or 'n': ")
        while hit == 'y':
            cardName = card_name(deck[0])
            print('You drew a', cardName)
            playerHand.extend(deck[0:1])
            del deck [0:1]
            print("Your hand is: ", end='')
            display_hand(playerHand)
            print("With a value of: ", end = '')
            print(hand_value(playerHand))
            hit = input("Would you like to hit? Press 'y' or 'n': ")

        # Dealer automatically hits if their hand has a value < 17
        while hand_value(dealerHand) < 17:
            dealerHand.extend(deck[0:1])
            del deck[0:1]

        # Reveal dealer hand after player is done hitting
        print("The dealer's hand is: ", end = '')
        display_hand(dealerHand)
        print("With a value of: ", end = '')
        print(hand_value(dealerHand))

        # Print results of the game
        if hand_value(dealerHand) > 21 and hand_value(playerHand) > 21:
            print('You and the dealer are both over 21. YOU BOTH LOSE!')
        elif hand_value(dealerHand) > 21 and hand_value(playerHand) <= 21:
            print('The dealer is over 21. YOU WIN!')
        elif hand_value(dealerHand) <= 21 and hand_value(playerHand) > 21:
            print('You are over 21. YOU LOSE!')
        elif hand_value(dealerHand) < hand_value(playerHand):
            print('YOU WIN!')
        else:
            print('YOU LOSE!')

    # Retry if initial player input is incorrect
    elif userIn != 'q':
        print('Invalid entry')
        main()

    # Quit game if user did not want to play
    else:
        print('Goodbye')

    #pass

#this function creates and ordered deck, shuffles, and returns the shuffled deck.
def generate_deck():
    suits = ['h','s','d','c']
    ranks = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
    deck = []

    for i in suits:
        for j in ranks:
            deck.append(j + i)

    random.shuffle(deck)
    
    return deck
    
#this function converts a card's string representation into a friendly, readable name
def card_name(card):
    rankDict = {'1':'Ace','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'Jack','12':'Queen','13':'King'}
    suitDict = {'h':'Hearts','s':'Spades','d':'Diamonds','c':'Clubs'}
    
    if len(card) < 3:
        rankName = rankDict[card[0]]
        suitName = suitDict[card[1]]
    if len(card) == 3:
        rankName = rankDict[card[0]+card[1]]
        suitName = suitDict[card[2]]

    cardName = rankName + " of " + suitName

    return cardName

#This function displays hand to player
def display_hand(hand):
    print(hand)
    
# This function calculates hand value
def hand_value(hand):
    handValue = 0
    aces = 0

    for i in hand:
        if len(i) < 3 and i[0] != '1':
            handValue += int(i[0])
        if len(i) == 3:
            handValue += 10
        if (len(i) < 3 and i[0] == '1'):
            aces += 1
            
        
    while aces > 0:
        if aces >= 2:
            handValue += 1
            aces -= 1
        elif handValue + 11 <= 21:
            handValue += 11
            aces -= 1
        else:
            handValue += 1
            aces -= 1
            
    return handValue
        
        
    

if __name__ == "__main__":
    main()