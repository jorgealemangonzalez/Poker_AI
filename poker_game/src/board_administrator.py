from board import Board
from libraries.deuces import *



class Board_administrator:
    def __init__(self):
        self.board = Board()
        self.deck = Deck()
    def cleanBoard(self):
        self.board = Board()
    def randomFullBoard(self):
        for i in range(5):
            self.board.addCard(self.deck.draw(1))
    def printBoard(self):
        print self.board.printBoard()