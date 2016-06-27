from libraries.deuces import *

class StaticsTable:
    nHands = 0                  #total number of hands registered of the player
    vpip = 0                    #voluntary put money in the pot
    vpipH = 0                   #vpip number of hands
    pfr = 0                     #pre flop raise
    pfrH = 0                    #pfr number of hands
#   refplayer                   #reference to the player

    def __init__(self,player):
        """
        player is a reference to Player class
        """
        self.refplayer = player
        
    def resetStatics(self):
        nHands = 0                  #total number of hands registered of the player
        vpip = 0                    #voluntary put money in the pot
        vpipH = 0                   #vpip number of hands
        pfr = 0                     #pre flop raise
        pfrH = 0                    #pfr number of hands
    
    
