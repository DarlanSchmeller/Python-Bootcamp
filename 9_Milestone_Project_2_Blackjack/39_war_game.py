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
    
class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create The Card Object
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # Check if it's a single card or a list
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

# Split Deck into half for each player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, is out of cards and has lost! Player Two Wins!')
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print('Player Two, is out of cards and has lost! Player One Wins!')
        game_on = False
        break

    # Start a new Round
    player_one_table_cards = []
    player_one_table_cards.append(player_one.remove_one())

    player_two_table_cards = []
    player_two_table_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_table_cards[-1].value > player_two_table_cards[-1].value:
            # Player 1 Won, give him all Table Cards
            player_one.add_cards(player_one_table_cards)
            player_one.add_cards(player_two_table_cards)

            at_war = False
        elif player_one_table_cards[-1].value < player_two_table_cards[-1].value:
            # Player 2 Won, give him all Table Cards
            player_two.add_cards(player_two_table_cards)
            player_two.add_cards(player_one_table_cards)

            at_war = False
        else:
            # WAR! Both players have the drawn cards with the same value
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print("Player One is unable to declare war, Player Two has won!")
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player Two is unable to declare war, Player One has won!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_table_cards.append(player_one.remove_one())
                    player_two_table_cards.append(player_two.remove_one())
                        