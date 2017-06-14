## 2017-06-09
## playing_cards.py
##
## Program to build a deck of cards using objects

import random

##----------------------------------------------------------------------------##
## Class to create cards. Strings are used to identify the suits
## and ranks of each card by using arrays
class Card:
    suits = ["Yellow", "Blue", "White", "Green", "Red"]
    ranks = ["blank", "W ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ",
             "8 ", "9 ", "10"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return (self.ranks[self.rank] + " " + self.suits[self.suit])

##----------------------------------------------------------------------------##
## Class to create and print the deck
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(5):
            for rank in range(1,2):
                self.cards.append(Card(suit, rank))
                self.cards.append(Card(suit, rank))
                self.cards.append(Card(suit, rank))
            for rank in range(2, 11):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s

    ## Function to shuffle cards. For every card in the deck it chooses a card at
    ## random and swaps positions with that card. Apparently this is a legitamate
    ## way to shuffle, according to some guy on the internet.
    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    ## Removes cards from the deck
    def remove(self,card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    ## Mechanism for taking cards from deck (technically from the bottom of the deck)
    def pop(self):
        return self.cards.pop()

    ## Deals cards. 
    def deal(self, hands, num_cards=16):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break
            card = self.pop()               ## take the top card
            hand = hands[i % num_hands]     ## whose turn is it to receive a card?
            hand.add(card)                  ## add the card to the hand

    ## True if the deck is empty
    def is_empty(self):
        return (len(self.cards) == 0)


##----------------------------------------------------------------------------##
## Class to make hands of cards, inherited from the Deck class

class Hand(Deck):
    def __init__(self, name = ''):
        self.cards = []
        self.name = name

    ## adds cards to the hand
    def add(self, card):
        self.cards.append(card)

##----------------------------------------------------------------------------##
## Class to set up card games

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

##----------------------------------------------------------------------------##
## Class to set up a game of Lost Cities

class LostCities(CardGame):
    def play(self, names):
        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(Hand(name))

        # Make the scoring columns
        self.columns = [[Hand("P1 Yellow"), Hand("P1 Blue"), Hand("P1 White"),
                        Hand("P1 Green"), Hand("P1 Red")],[Hand("P2 Yellow"),
                        Hand("P2 Blue"), Hand("P2 White"), Hand("P2 Green"),
                        Hand("P2 Red")]]

        # Make the discard piles
        suits = ["Yellow", "Blue", "White", "Green", "Red"]
        self.discard = []
        
        for suit in suits:
            self.discard.append(Hand(suit))
            
        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Initial hands ----------")
        self.printGame()
        
        # Play until the cards run out. Turn is who's turn it is, numHands is number
        # of players
        turn = 0
        numHands = len(self.hands)
        while not self.deck.is_empty():
            self.playOneTurn(turn)
            turn = (turn + 1) % numHands

        print("---------- Game is Over -----------")
        self.printGame()
        
    def playOneTurn(self, player):
        self.placeCard(player)
  ##      self.pickCard(player)

    def placeCard(self, turn_place):
        pickedCard = self.hands[turn_place].pop()
        
##
##    def pickCard(self, turn_pick):
##        ##
    
    def printGame(self):
        for hand in self.hands:
            print(hand.name)
            print(hand)

        for x in range(0 , 2):
            print(self.hands[x].name)
            for column in self.columns[x]:
                print(column.name)
                print(column)
                
        print("Discard Piles")
        for pile in self.discard:
            print(pile.name)
            print(pile)

                
##----------------------------------------------------------------------------##
## Main

def main():
    game = LostCities()
    game.play(["Ryan", "Stephen"])
    
main()   



