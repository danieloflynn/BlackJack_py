class Card():
    #     Instance suits and values
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    values = (None, None, '2', '3', '4', '5', '6', '7', '8',
              '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    shortValues = (None, None, '2', '3', '4', '5', '6', '7', '8',
                   '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, suitidx, valueidx):
        #         Check if suit and value in range
        if 0 <= suitidx < len(self.suits) and 0 < valueidx < len(self.values):
            self.suit = self.suits[suitidx]
            self.value = self.values[valueidx]
            self.suitidx = suitidx
            self.valueidx = valueidx
#             Print error message if not
        else:
            print("Error: suit or value idx out of range")

    def showShortValue(self):
        return self.shortValues[self.valueidx]

#         Reveals the current card
    def __str__(self):
        return str(self.value) + " of " + str(self.suit)


#     check if suit and value are equal

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False

#    check if value less than
    def __lt__(self, other):
        if self.valueidx < other.valueidx:
            return True
        else:
            return False

#    check if value greater than
    def __gt__(self, other):
        if self.valueidx > other.valueidx:
            return True
        else:
            return False

    # represent value
    def __repr__(self):
        return self.__str__()


c = Card(1, 11)
repr(c)
