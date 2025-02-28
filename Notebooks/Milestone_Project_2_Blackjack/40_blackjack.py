# Milestone Project 2 - Blackjack Game

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.all_deck_cards = []

        for rank in ranks:
            for suit in suits:
                self.all_deck_cards.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(self.all_deck_cards)

    def __str__(self):
        deck_comp = ''
        for card in self.all_deck_cards:
            deck_comp += f'\n {card.__str__()}'
        return f"The deck has: {deck_comp}"
    
    def deal(self):
        single_card = self.all_deck_cards.pop()
        return single_card
        
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card): 
        self.cards.append(card)
        self.value += values[card.rank]

        # Track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # Adjust ace value to be 1 if the total value is higher than 21 and player still has an ace
        while self.value > 21 and self.aces:
            self.value -+ 10
            self.aces -+ 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet

def take_bet(chips):
    while True:
        try:
            bet_value = int(input("Insert how many chips you'd like to bet:"))

            if type(bet_value) == int and bet_value > 0 and bet_value <= chips.total:
                chips.bet += bet_value
            else:
                print(f"You don't have this amount available to bet. You have {chips.total}")
        except:
            return "You can't bet this value, please insert an integer number"
        else:
            break

def take_hit(deck, hand):
    single_card = deck.deal()
    hand.cards.append(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        response = input("Hit or Stand (H/S): ").lower()

        if response[0] == 'h':
            print("Player Hits!")
        elif response[0] == 's':
            print("Player Stands, Dealers Turn!")
            playing = False
        else:
            print('Sorry, I did no understand that, please enter H or S only!')

def show_some(player, dealer):
    # Show only one of the dealer's cards
    print("\n Dealer's Hand:")
    print("First Card Hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of the player's hand
    print("\n Player's Hand:")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # Show all player's cards
    for card in player.cards:
        print(card)
    print(f"The Value of the Player's hand is: {player.value}")

    # Show all Dealer's cards
    for card in dealer.cards:
        print(card)
    print(f"The Value of the Dealer's hand is: {dealer.value}")

    ## A simpler way to print all items in a list, use an *
    # print(*dealer.cards)

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS!BUST DEALER!")
    chips.lose_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.win_bet()

def push(player, dealer):
    print("Player and Dealer have both hit 21, the game is a TIE! PUSH!")