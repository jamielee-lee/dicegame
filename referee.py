# Jamie Lee
# CS 333
# Final Project
# Referee

from die import Die
import random

class Referee:
    def __init__(self):
        self.name = "Rule Enforcer :)"
        self.roundEnd = 0

    # integration between referee and die
    def rollAdvantageDie(self):
        die = Die()

        # roll 1 dice
        return random.choices(die.faces, weights=die.probabilities)

    # integration between referee and player
    def determinePlayerAdvantage(self, player1, player2):
        player1.advantage = 0
        player2.advantage = 0

        while (player1Advantage == player2Advantage):
            player1Advantage = self.rollAdvantageDie()
            player2Advantage = self.rollAdvantageDie()

            if (player1Advantage > player2Advantage):
                player1.advantage = 1
                break
            else:
                if (player1Advantage < player2Advantage):
                    player2.advantage = 1
                    break

    # integration between player and die
    def checkSameSum(self, player1, player2):
        if (sum(player1.dice) == sum(player2.dice)):
            # if both player rolled two 0's
            if (player1.die1 == 0 & player1.die2 == 0 & player2.die1 == 0 & player2.die2 == 0):
                if (player1.advantage == 1):
                    # player 2 loses
                    return -2
                else:
                    # player 1 loses
                    return -1
            # otherwise if players rolled the same sum, reroll
            else:
                return 1
        else:
            return 0
        
    def checkZero(self, player1, player2):
        if (sum(player1.dice) == sum(player2.dice)):
            # if both player rolled two 0's
            if (player1.die1 == 0 & player1.die2 == 0 & player2.die1 == 0 & player2.die2 == 0):
                if (player1.advantage == 1):
                    # player 2 loses
                    return -2
                else:
                    # player 1 loses
                    return -1
            # otherwise if players rolled the same sum, reroll
            else:
                return 1
        else:
            return 0

    # integration between player and die
    def checkDice(self, player1, player2):
        if (self.checkSameSum(player1, player2) == 1):
            return 1
        elif (sum(player1.dice) > sum(player2.dice)):
            # player 1 wins the round
            player1.roundWins += 1
        elif (sum(player1.dice) < sum(player2.dice)):
            # player 2 wins the round
            player2.roundWins += 1
        elif (self.checkSameSum(player1, player2) == -1):
            self.triggerGameOver(player2)
        elif (self.checkSameSum(player1, player2) == -2):
            self.triggerGameOver(player1)


    def checkRoundWins(self, player1, player2):
        if (player1.roundWins == 5):
            self.triggerGameOver(player1)
            return 1
        
        if (player2.roundWins == 5):
            self.triggerGameOver(player2)
            return 1


    def triggerGameOver(self, player):
        # Game Over Conditions...
        # Player 1 rolls two 0's
        # Player 2 rolls two 0's
        # A player has won 5 rounds
        print("\n\n" + player.name + " has won! yippee")