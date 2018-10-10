#Firstly we have to import all the necessary packages to effectively run the program"""

import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard
import sys

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

class BlackjackGame:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        self.players = players
        self.scores = {}
        print("Created a game with {} players.".format(len(self.players)))
		
		
    def black_jack(self):     #The main blackjack game sequence. Each player takes an entire turn before moving on.  If each player gets a turn and no one has won, the player or players with the highest score below 21 are declared the winner.
        print("The Game is Setting up to Play...")
        print("Shuffling The Card...")
        self.deck.shuffle()
        print("The Card is All shuffled!")
        print("Dealing...")
        self.deal()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn to play...".format(player.name))
            self.play(player)
        else:
            print("That's the last turn. Getting the winner...")
            self.find_winner()

    def deal(self):
        for _ in range(5):
            for p in self.players:
                newcard = self.deck.draw()
                p.hand.append(newcard)       #Shares Five cards to each of the player.
                print("Dealt {} the {}.".format(p.name, str(newcard)))

    def find_the_winner(self):
       
        winners = []			
        try:
            winning_score = max(self.scores.values())   #First find the highest score and find the players with the highest score
            for key in self.scores.keys():
                if self.scores[key] == winning_score:
                    winners.append(key)
                else:
                    pass
            win_string = " & ".join(winners)
            print("And the winner is...{}!".format(win_string))
        except ValueError:
            print("Whoops! Everybody lost!")

    def hit(self, player):
       
        newcard = self.deck.draw()
        player.hand.append(newcard)   ##Adds a card to the player's hand and states which card was drawn
        print("   Drew the {}.".format(str(newcard)))

    def play(self, player):   # An individual player's turn.
        
        while True:
            points = sum_hand(player.hand)

            if points < 17:        # If the player's cards are an ace and a ten or court card,the player has a blackjack and wins.
                print("   Hit.")
                self.hit(player)
            elif points == 21:  			# If a player's cards total more than 21, the player loses.
                print("   {} wins!".format(player.name))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else: 		 #  Otherwise, it takes the sum of their cards and determines whetherto hit or stand based on their current score.
                print("   Standing at {} points.".format(str(points)))
                self.scores[player.name] = points
                break

def sum_hand(hand: list):
    vals = [card.rank for card in hand]   
    intvals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:  #Converts ranks of cards into point values for scoring purposes.'K', 'Q', and 'J' are converted to 10.'A' is converted to 1 (for simplicity), but if the first hand is an ace and a 10-valued card, the player wins with a blackjack.
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  # adding 1 to intvals
    if intvals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("mansi"), Player("soni"), Player("Taw"),
        Player("ramya")])
    game.black_jack()
