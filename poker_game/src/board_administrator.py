from board import Board
from libraries.deuces import *



class Board_administrator:							#Means the dealer
    def __init__(self):
        self.board = Board()
        self.deck = Deck()
        self.evaluator = Evaluator()
	
    def cleanBoard(self):
        self.board = Board()
		
    def randomFullBoard(self):
        self.deck.shuffle()
        self.board.clean()
        for i in range(5):
            self.board.addCard(self.deck.draw(1))
			
    def printBoard(self):
        print self.board.printBoard()
                        
    def dealPlayer(self):
        return self.deck.draw(2)
                        
    def getEquityOnePlayer(self,pairCards):
        return self.evaluator.evaluate(self.board.getBoard(),pairCards)
    
