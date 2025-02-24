# CARD
# Understand the Suit of the Card
# Understand the rank of the Card
# Easy to use integer Value (For comparing values of cards)

# Deck Class
# 52 cards that come into a deck

# Player who can hold cards
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
        'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit
    



two_hearts = Card('Hearts', "Two")
print(two_hearts)
print(two_hearts.value)
print(two_hearts.suit)

three_of_clubs = Card('Clubs', "Three")
print(three_of_clubs)
print(three_of_clubs.value)
print(three_of_clubs.suit)


print(two_hearts.value > three_of_clubs.value)