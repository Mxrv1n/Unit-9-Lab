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

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()
    
    def win_coin(self):
        self.__wallet+=1

    def lose_coin(self):
        self.__wallet-=1
    
    def get_wallet(self):
        return self.__wallet
    
    def get_name(self):
        return self.__name