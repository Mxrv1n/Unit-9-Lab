''''Name: Lab9_mperez55
Author: Marvin Perez
Purpose:  Coin file for coins class.
Date: 03/10/2026'''
import random

class Coin:
    def __init__(self):

        """Initialize coin with either heads or tails."""
        if random.randint(0,1) == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = "heads"
        else:
            self.__sideup = "tails"
    def get_sideup(self):
        return self.__sideup
