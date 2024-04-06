class PlayCard:

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def get_suit(self):
        return self._suit

    def get_value(self):
        return self._value
