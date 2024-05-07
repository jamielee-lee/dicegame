# Jamie Lee
# CS 333
# Final Project
# Player

from die import Die
import random

class Player:
    def __init__(self):
        self.name = ""
        self.advantage = 0

        self.dice = []

        self.wins = 0

    # integration between player and die
    def rollDice(self):
        die = Die()

        # roll 2 dice
        self.dice = random.choices(die.faces, weights=die.probabilities, k=2)
