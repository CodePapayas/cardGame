import random
from play_card import PlayCard


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []

    for suit in suits:
        for value in values:
            deck.append(PlayCard(suit, value))

    random.shuffle(deck)
    return deck


class BlackjackGame:

    def __init__(self):
        card_deck = create_deck()
        self._card_deck = card_deck
        self._player_hand = []
        self._dealer_hand = []
        self.initial_deal()

    def initial_deal(self):
        for _ in range(2):
            self._dealer_hand.append(self._card_deck.pop())
            self._player_hand.append(self._card_deck.pop())

    def player_hit(self):
        self._player_hand.append(self._card_deck.pop())

