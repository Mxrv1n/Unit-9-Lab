''''Name: Lab9_mperez55
Author: Marvin Perez
Purpose: Player file for Player class.
Date: 03/10/2026'''
from coin import Coin

class player:
    def __init__(self,name="Player 1"):
        self.__name  = name
        self.__wallet = 20
        self.__coin = Coin() 

    #REMOVE LATER
    def __printname__(self):
        print(self.__name)