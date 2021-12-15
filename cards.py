from random import shuffle
from card import Card


class Cards:
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    colors = ['club', 'diamond', 'heart', 'spade']
    deck = []
    count = len(deck)

    def __init__(self):
        for color in self.colors:
            for value in self.values:
                self.deck.append(Card(value, color))

    def getCards(self):
        return self.deck

    def getCount(self):
        return self.count

    def shuffle(self):
        shuffle(self.deck)

    def draw(self):
        return self.deck.pop()
