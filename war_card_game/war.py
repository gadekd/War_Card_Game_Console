import random

# H = Hearts (Kier)
# D = Diamonds (Karo)
# S = Spades (Pik)
# C = Clubs (Trefl)

SYMBOLS = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Nice way to add every element to one list to every element of second list
deck = [a + b for a in RANKS for b in SYMBOLS]
shuffled_deck = random.sample(deck, len(deck))

deck_a = []
deck_b = []

for index, card in enumerate(shuffled_deck):
    if index < int(len(shuffled_deck) / 2):
        deck_a.append(card)
    else:
        deck_b.append(card)

# print(SYMBOLS)
# print(RANKS)
# print('Normal deck:', deck)
# print('Shuffled deck:', shuffled_deck)
# print('Deck A:', deck_a, len(deck_a))
# print('Deck B:', deck_b, len(deck_b))

class Deck:
    def __init__(self):
        print('Creating a deck')
        self.deck = [a + b for a in SYMBOLS for b in RANKS]
    
    # Shuffle card deck
    def shuffle_deck(self):
        print('Shuffling cards')
        self.shuffled_deck = random.sample(self.deck, len(self.deck))
    
    # Distribute cards among players - each should have 26 cards
    def distribute_cards(self):
        # First player's deck
        self.deck_a = []
        # Second player's deck'
        self.deck_b = []

        for index, card in enumerate(self.shuffled_deck):
            if index < int(len(self.shuffled_deck) / 2):
                self.deck_a.append(card)
            else:
                self.deck_b.append(card)
                
        # return 'Deck A: {} Deck size: {} cards\nDeck B: {} Deck size: {} cards'.format(self.deck_a, len(self.deck_a), self.deck_b, len(self.deck_b))
        return self.deck_a, self.deck_b
                

class Hand:
    # Each player has a hand
    def __init__(self, cards):
        self.cards = cards
        
    # How many cards does the hand have
    def __str__(self):
        return 'This hand has {} cards.'.format(len(self.cards))

    # Add card method
    def add_card(self, added):
        self.cards.extend(added)
        # print('Added {} cards'.format(len(self.added)))
    
    # Remove card method
    def remove_card(self):
        return self.cards.pop()

class Player:
    # Each player has name and instance of the Hand class
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        print('I am {} and I have a hand! Here it is: {}'.format(self.name, self.hand))
    
    # Method to play card
    def play_card(self):
        # This is card that player plays with at the moment
        # It removes card from player's hand and place it on the table - it is now in game
        drawn_card = self.hand.remove_card()
        print('{} has placed: {}\n'.format(self.name, drawn_card))
        return drawn_card
    
    # Method to draw cards to war array
    def war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop(0))
            return war_cards
            
    
    # Method to check if Player have cards
    def check_deck(self):
        # If the player still has cards to play with, return True
        return len(self.hand.cards) != 0
    
    def check_cards_amount(self):
        if len(self.hand.cards) > 1:
            return '{} has {} more cards.'.format(self.name, len(self.hand.cards))
        else:
            return '{} has only 1 more card!.'.format(self.name)


# GAME =================================================================================

# Firstly, let's create deck of cards and divide it in half
deck_of_cards = Deck()
deck_of_cards.shuffle_deck()

# Distribute_cards() returns two values, so we can assign them to corresponding decks
deck_a, deck_b = deck_of_cards.distribute_cards()

print('Deck A:', Hand(deck_a))
print('Deck B:', Hand(deck_b))

print(deck_a)
print(deck_b)

# Make players
computer = Player('Gus', Hand(deck_a))
# players_name = input('Enter your name to start the game of War: ')
player = Player('Daniel', Hand(deck_b))

# War counter
how_many_wars = 0

# Round counter
how_many_rounds = 0

while computer.check_deck() and player.check_deck():
    how_many_rounds += 1

    # Game list
    cards_to_compare = []

    # Computer's card
    computer_card = computer.play_card()
    # Player's card
    player_card = player.play_card()

    cards_to_compare.append(computer_card)
    cards_to_compare.append(player_card)

    print(computer.check_deck())

    print(computer.check_cards_amount())

    print('HERE', cards_to_compare)

    if computer_card[1] == player_card[1]:
        how_many_wars +=1
        print("War occured! Brace yourself!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        cards_to_compare.extend(player.war_cards())
        print('War cards: ', player.war_cards())
        cards_to_compare.extend(computer.war_cards())
        print('War cards: ', computer.war_cards())

        # Play cards
        computer_card = computer.play_card()
        player_card = player.play_card()

        # Add to table_cards
        cards_to_compare.append(computer_card)
        cards_to_compare.append(player_card)

        # Check to see who had higher rank
        if RANKS.index(computer_card[1:]) < RANKS.index(player_card[1:]):
            print(player.name+" has the higher card, adding to hand.")
            player.hand.add_card(cards_to_compare)
        else:
            print(computer.name+" has the higher card, adding to hand.")
            computer.hand.add_card(cards_to_compare)
        
        # Player with higher card takes it all - 6 cards on the table!
    else:
        # This is scenario if we don't have a war; we can now check for the cards' ranks | ELSE STATEMENT FOR BIG IF
        if RANKS.index(computer_card[1:]) > RANKS.index(player_card[1:]):
            print('Wygrywa Gus. Oto jego karta: {}'.format(cards_to_compare[0]))
            computer.hand.add_card(cards_to_compare)
            print(cards_to_compare)
        else:
            print('Wygrywa Daniel. Oto jego karta: {}'.format(cards_to_compare[1]))
            player.hand.add_card(cards_to_compare)
            print(cards_to_compare)


print('Game over...')
print('The game lasted {} rounds.'.format(how_many_rounds))
print('War occured {} times.'.format(how_many_wars))
