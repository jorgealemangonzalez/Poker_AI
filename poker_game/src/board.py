# Jorge Aleman Gonzalez 
from libraries.deuces import *
import random

#numbers = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]

class Board:
    board = []     
    def __init__(self):
        print("Boards has init")
        
    def addCard(self,card):                                                     #card is instance of Card
        self.board.append(card)
    def getBoard(self):
        return self.board
    def printBoard(self):
        Card.print_pretty_cards(self.board)
    def clean(self):
        self.board = []
        
