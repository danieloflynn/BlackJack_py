import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
#         4 suits
        for suit in range(0, 4):
            #         14 values (9 value, 3 face, 1 ace)
            for value in range(2, 15):
                self.cards += [Card(suit, value)]
#             shuffle the cards
        random.shuffle(self.cards)
        self.original = self.cards.copy()

#     removes a card from the deck and returns it
    def draw(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return

    def drawCards(self, numCards):
        # Draws numCards cards from the deck, returns a list of card objects
        if len(self.cards) >= numCards:
            cards = []
            for _ in range(numCards):
                cards += [self.draw()]
            return cards
        return

#     Reveals the whole deck of cards
    def __str__(self):

        string = "Cards in Deck:\n"
        for card in self.cards:
            string += str(card) + "\n"
        return string

#     Shuffles the cards again
    def shuffle(self):
        random.shuffle(self.cards)

#    Resets the deck to its original state
    def reset(self):
        self.cards = self.original.copy()

    def newDeck(self):
        self.reset()
        self.shuffle()

    def sort_by_value(self):
        self.cards.sort(key=lambda card: (card.values.index(
            card.value), card.suits.index(card.suit)))

#         sorts the cards by suit then value
    def sort_by_suit(self):
        self.cards.sort(key=lambda card: (card.suits.index(
            card.suit), card.values.index(card.value)))

    # Sort the cards by value but not by suit
    def sort(self):
        self.cards.sort()

    # Returns the num cards left
    def __len__(self):
        return len(self.cards)
