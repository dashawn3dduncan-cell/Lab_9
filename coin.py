"""
Program: The Coin Class
Name: Dashawn Duncan
Purpose: Create a class that represents a coin.
Date: 3/13/2026
"""

import random

class Coin:

    def __init__(self):
        self.toss()

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup 