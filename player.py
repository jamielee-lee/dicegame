# Jamie Lee
# CS 333
# Final Project
# Player

from die import Die
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.advantage = 0

        self.dice = []

        self.die1 = 0
        self.die2 = 0

        self.roundWins = 0
        self.gameWins = 0

    # integration between player and die
    def rollDice(self):
        die = Die()

        # roll 2 dice
        self.dice = random.choices(die.faces, weights=die.probabilities, k=2)

        self.die1 = self.dice[0]
        self.die2 = self.dice[1]
