#-*- coding: utf-8 -*-
from libraries.deuces import *
#import libraries.colorama
from board_administrator import Board_administrator
from player import Player
__author__ = "jorge"
__date__ = "$15-may-2016 12:41:59$"

if __name__ == "__main__":
    admin = Board_administrator()
    p1 = Player(Player.BT)
    p2 = Player(Player.BT)
    admin.randomFullBoard()
    admin.printBoard()
    admin.addPlayer(p1)
    admin.addPlayer(p2)
    admin.dealPlayers()
    p1.printHand()
    p2.printHand()
    #print "Has equity "
    #print admin.getEquityOnePlayer(h1)
