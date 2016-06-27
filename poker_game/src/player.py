from staticsTable import StaticsTable
from libraries.deuces import *
class Player:
#    movements
    CHECK = 0
    CALL = 1
    RAISE = 2
    
#    positions
    BT = 0          #button
    SB = 1          #small blind
    BB = 2          #big blind
    UTG = 3         #under the gun
    UTG1 = 4        #under the gun +1
    UTG2 = 5        #under the gun +2
    MD = 6          #middium position
    MD1 = 7         #middium position +1
    MD2 = 8         #middium position +2
    CO = 9          #cut off
    
#    table          #reference to the  staticsTable of the player
    nick = ""       #name of the player
    hand = []       #pair of cards
    position = 0

    def __init__(self,position):
        self.table = StaticsTable(self)
        self.position = position
        
    def getNick(self):
        return self.nick
    def setNick(self,nick):
        self.nick = nick

    def getHand(self):
        return self.hand

    def printHand(self):
        Card.print_pretty_cards(self.hand)

    def getTable(self):
        return self.table

    def move(self,moveTipe,amount):
        print "the player "+self.nick+ " moves"

    def passMove(self,amount):
        print "it pass"

    def callMove(self,amount):
        print "it calls"

    
        
        
        
