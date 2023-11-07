from card import Card


class Player:

    cardValues = {
        "Ace": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10
    }
    # Takes in name as string and cash as float

    def __init__(self, name: str, cash: float):
        self.wins: int = 0
        self.bet: float = 0
        self.cardsHeld: [Card] = []
        self.name: str = name
        self.cash: float = cash

    # Add a win to the player
    def win(self):
        self.wins += 1

    # Lose
    def lose(self):
        return

    # Change the card held by the player
    def giveCard(self, card: Card):
        self.cardsHeld += [card]

    def giveCards(self, cards: [Card]):
        self.cardsHeld += cards

    def newHand(self):
        self.cardsHeld = []

    def getHand(self):
        # shows the hand currently held
        return [c.value for c in self.cardsHeld]

    def showShortHand(self):
        # Shows the hand the player has in format A 10 etc.
        if self.cardsHeld == []:
            return
        cards = ""
        for card in self.cardsHeld:
            cards += card.showShortValue() + " "
        return cards

    def revealCard(self, idx):
        # Shows the card at index idx
        if idx < len(self.cardsHeld):
            return self.cardsHeld[idx].showShortValue()
        return

    def makeBet(self):
        while True:
            bet = float(input(f'{self.name}, please enter a bet amount'))
            if bet <= self.cash:
                self.cash -= bet
                self.bet = bet
                break
            else:
                print(
                    f'Insufficient cash to make bet, you currently have {self.cash}')

    def evaluateHand(self):
        # count num of aces
        aceCount = 0
        # Accumulate total
        total = 0
        for card in self.getHand():
            # If ace, increment count
            if card == "Ace":
                aceCount += 1
            total += self.cardValues[card]
        # If you have an ace and you are going bust, reduce the ace value by 10 (Ace can be 11 or 1)
        for _ in range(aceCount):
            if total > 21:
                total -= 10
        return total

    def __str__(self):
        return f'{self.name}, cash held: {self.cash}, cards held: {self.cardsHeld}'
