import time
from player import Player
from deck import Deck


class BlackJack:

    def __init__(self, numPlayers):
        self.players: [Player] = []
        if numPlayers < 2:
            print("Error: There must be at least 2 players")
        self.dealer = Player(
            input(f'Dealer, please enter your name: '), 1000000)
        for i in range(numPlayers - 1):
            self.players.append(
                Player(input(f'Player {i + 1} Please enter your name: '), 10000))
        self.deck = Deck()

    def play(self):
        # Plays the game

        # Loop until broken out
        while (True):
            self.dealNewHand()  # Clears the hands of all players and deals a new hand
            # Iterate through all players and deal each a hand
            for player in self.players:
                # Print the player's name
                self.gamePrint(f'It\'s {player.name}\'s turn.')
                playerHand = player.evaluateHand()
                self.gamePrint(
                    f'You are holding {player.showShortHand()}, value {playerHand}')
                if playerHand == 21:
                    self.gamePrint("BlackJack!")
                while playerHand < 21:
                    if input('Hit? y/[n]') == 'y':
                        newCard = self.deck.draw()
                        player.giveCard(newCard)
                        playerHand = player.evaluateHand()
                        self.gamePrint(f'{player.name} drew {newCard}')
                        self.gamePrint(
                            f'You are holding {player.showShortHand()}, value {playerHand}')
                        if playerHand > 21:
                            self.gamePrint(f'{player.name} has gone bust!')
                    else:
                        break
            self.gamePrint(f'It\'s the dealer\'s turn')
            playerHand = self.dealer.evaluateHand()
            self.gamePrint(
                f'You are holding {self.dealer.showShortHand()}, value {playerHand}')
            if playerHand == 21:
                self.gamePrint("BlackJack!")
            while playerHand < 21:
                if input('Hit? y/[n]') == 'y':
                    newCard = self.deck.draw()
                    self.dealer.giveCard(newCard)
                    playerHand = self.dealer.evaluateHand()
                    self.gamePrint(f'Dealer drew {newCard}')
                    self.gamePrint(
                        f'You are holding {self.dealer.showShortHand()}, value {playerHand}')
                    if playerHand > 21:
                        self.gamePrint(f'Dealer has gone bust!')
                else:
                    break
            for player in self.players:
                if player.evaluateHand() > 21:
                    player.lose()
                    self.gamePrint(f'{player.name} lost')
                elif self.dealer.evaluateHand() > 21:
                    player.win()
                    self.gamePrint(f'{player.name} won')
                elif self.dealer.evaluateHand() == player.evaluateHand():
                    self.gamePrint(f'{player.name} drew')
                elif player.evaluateHand() > self.dealer.evaluateHand():
                    self.gamePrint(f'{player.name} won')
                    player.win()
                else:
                    player.lose()
                    self.gamePrint(f'{player.name} lost')

            if input("Play another hand? [y]/n: ") == "n":
                break
            # Reset the deck
            self.deck.newDeck()

    def gamePrint(self, text):
        time.sleep(1)
        print(text)

    def numPlayers(self):
        return len(self.players) + 1

    def evaluateHand(self, Player):
        # count num of aces
        aceCount = 0
        # Accumulate total
        total = 0
        for card in Player.getHand():
            # If ace, increment count
            if card.value == "Ace":
                aceCount += 1
            total += self.cardValues[card.value]
        # If you have an ace and you are going bust, reduce the ace value by 10 (Ace can be 11 or 1)
        for i in range(aceCount):
            if total > 21:
                total -= 10

    def dealNewHand(self):
        # Deal cards to the dealer
        # self.dealer.giveCard(self.deck.draw())
        self.dealer.newHand()
        self.dealer.giveCards(self.deck.drawCards(2))

        self.gamePrint(f'Dealer is showing {self.dealer.revealCard(0)}')
        # Deal cards to each player
        for player in self.players:
            player.newHand()
            player.giveCards(self.deck.drawCards(2))
