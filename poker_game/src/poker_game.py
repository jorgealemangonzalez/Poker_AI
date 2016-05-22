#-*-coding: utf-8 -*-
from libraries.deuces import *
import libraries.colorama
from board_administrator import Board_administrator

__author__ = "jorge"
__date__ = "$15-may-2016 12:41:59$"

if __name__ == "__main__":
    admin = Board_administrator()
    admin.randomFullBoard()
    admin.printBoard()
 