# Jamie Lee
# CS 333
# Final Project
# Referee

from die import Die
import random

class Referee:
    def __init__(self):
        self.name = ""
        self.advantage = 0

        self.dice = []

        self.wins = 0

    # 
    def checkAdvantage(self):
        die = Die()

        # roll 2 dice
        self.dice = random.choices(die.faces, weights=die.probabilities, k=2)
