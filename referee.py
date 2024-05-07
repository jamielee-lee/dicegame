# Jamie Lee
# CS 333
# Final Project
# Referee

from die import Die
import random

class Referee:
    def __init__(self):
        self.name = "Game Master - Rule Enforcer :)"
        self.roundEnd = 0

    # integration between referee and die
    def rollAdvantageDie(self):
        die = Die()

        # roll 1 dice
        return random.choices(die.faces, weights=die.probabilities)

    def setPlayerAdvantage(self):
        player1Advantage = self.rollAdvantageDie()
        player2Advantage = self.rollAdvantageDie()

        if (player1Advantage == player2Advantage):
            return [0, 0]
        else:
            return [player1Advantage, player2Advantage]
        
    # 
    def determinePlayerAdvantage(self, player1, player1Advantage, player2, player2Advantage):
        if (player1Advantage > player2Advantage):
            player1.advantage = 1
        elif (player1Advantage < player2Advantage):
                player2.advantage = 1
        else:
            return 0

    # integration between player and die
    def checkSameSum(self, player1, player2):
        if (sum(player1.dice) == sum(player2.dice)):
            # if both player rolled two 0's
            if (player1.die1 == 0 and player1.die2 == 0 and player2.die1 == 0 and player2.die2 == 0):
                if (player1.advantage == 1):
                    # player 2 loses
                    return -2
                else:
                    # player 1 loses
                    return -1
            # if both players rolled two 10's
            elif (player1.die1 == 10 and player1.die2 == 10 and player2.die1 == 10 and player2.die2 == 10):
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
            # players did not have the same sum
            return 0
        
    def checkDoubles(self, player1, player2):
        if (player1.die1 == 0 and player1.die2 == 0):
            player2.roundWins = 5
            return 1
        elif (player2.die1 == 0 and player2.die2 == 0):
            player1.roundWins = 5
            return 1
        elif (player1.die1 == 10 and player1.die2 == 10):
            player1.roundWins = 5
            return 1
        elif (player2.die1 == 10 and player2.die2 == 10):
            player2.roundWins = 5
            return 1
        else:
            return 0
        
    def checkZero(self, player1, player2):
        if (0 in player1.dice or 0 in player2.dice):
            if (player1.advantage == 1):
                if (0 in player1.dice):
                    player1.roundWins += 1
                elif (0 in player2.dice):
                    player2.roundWins += 1
            else:
                if (0 in player2.dice):
                    player2.roundWins += 1
                elif (0 in player1.dice):
                    player1.roundWins += 1

            return 1
        else:
            return 0

    def checkTen(self, player1, player2):
        if (10 in player1.dice or 10 in player2.dice):
            if (player1.advantage == 1):
                if (10 in player2.dice):
                    player1.roundWins += 1
                elif (10 in player1.dice):
                    player2.roundWins += 1
            else:
                if (10 in player1.dice):
                    player2.roundWins += 1
                elif (10 in player2.dice):
                    player1.roundWins += 1

            return 1
        else:
            return 0

    def checkZeroTen(self, player1, player2):
        if (10 in player1.dice and 0 in player1.dice):
            return 1
        elif (10 in player2.dice and 0 in player2.dice):
            return 1
        else:
            return 0

    # integration between player and die
    def checkDice(self, player1, player2):
        if (self.checkSameSum(player1, player2) == -1):
            self.triggerGameOver(player2)
            return -1
        elif (self.checkSameSum(player1, player2) == -2):
            self.triggerGameOver(player1)
            return -2
        elif (self.checkDoubles(player1, player2) == 1):
            self.checkRoundWins(player1, player2)
            return 2
        elif (self.checkZeroTen(player1, player2) == 1):
            return 1
        elif (self.checkZero(player1, player2) == 1 or self.checkTen(player1, player2) == 1):
            return 0
        elif (self.checkSameSum(player1, player2) == 1):
            return 1
        elif (sum(player1.dice) > sum(player2.dice)):
            # player 1 wins the round
            player1.roundWins += 1
        elif (sum(player1.dice) < sum(player2.dice)):
            # player 2 wins the round
            player2.roundWins += 1


    def checkRoundWins(self, player1, player2):
        if (player1.roundWins == 5):
            self.triggerGameOver(player1)
            return 1
        elif (player2.roundWins == 5):
            self.triggerGameOver(player2)
            return 2
        else:
            return 0

    def triggerGameOver(self, player):
        print("\n\n" + player.name + " has won! yippee")

        return player.name

    def resetPlayer(self, player):
        player.dice = []
        player.roundWins = 0

    def resetReferee(self):
        self.roundEnd = 0

    def resetGame(self, player1, player2):
        self.resetPlayer(player1)
        self.resetPlayer(player2)
        self.resetReferee()