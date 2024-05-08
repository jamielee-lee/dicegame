# Jamie Lee
# CS 333
# Final Project
# Referee Unit Tests

from referee import Referee
from player import Player
import unittest

class TestPlayerMethods(unittest.TestCase):
    def test_determinePlayerAdvantage(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        p1.advantage = 0
        p2.advantage = 0

        # if both dice rolls are same
        self.assertEqual(ref.determinePlayerAdvantage(p1, 10, p2, 10), 0)

        p1.advantage = 0
        p2.advantage = 0

        # if p1 wins advantage roll
        ref.determinePlayerAdvantage(p1, 10, p2, 2)
        self.assertEqual(p1.advantage, 1)
        self.assertEqual(p2.advantage, 0)

        p1.advantage = 0
        p2.advantage = 0

        # if p2 wins advantage roll
        ref.determinePlayerAdvantage(p1, 1, p2, 6)
        self.assertEqual(p1.advantage, 0)
        self.assertEqual(p2.advantage, 1)

    def test_checkSameSum(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if both players rolled two 0's and p1 has advantage
        # p2 should lose
        p1.advantage = 1
        p2.advantage = 0
        p1.die1, p1.die2 = 0, 0
        p2.die1, p2.die2 = 0, 0

        self.assertEqual(ref.checkSameSum(p1, p2), -2)

        # if both players rolled two 0's and p2 has advantage
        # p1 should lose
        p1.advantage = 0
        p2.advantage = 1
        p1.die1, p1.die2 = 0, 0
        p2.die1, p2.die2 = 0, 0

        self.assertEqual(ref.checkSameSum(p1, p2), -1)
        
        # if both players rolled two 10's and p1 has advantage
        # p1 should win/p2 should lose
        p1.advantage = 1
        p2.advantage = 0
        p1.die1, p1.die2 = 10, 10
        p2.die1, p2.die2 = 10, 10

        self.assertEqual(ref.checkSameSum(p1, p2), -2)

        # if both players rolled two 10's and p2 has advantage
        # p2 should win/p1 should lose
        p1.advantage = 0
        p2.advantage = 1
        p1.die1, p1.die2 = 10, 10
        p2.die1, p2.die2 = 10, 10

        self.assertEqual(ref.checkSameSum(p1, p2), -1)

        # if none of the above occurs and both players rolled the same sum
        p1.dice = [5, 1]
        p2.dice = [2, 4]
        p1.die1, p1.die2 = 5, 1
        p2.die1, p2.die2 = 2, 4

        self.assertEqual(ref.checkSameSum(p1, p2), 1)

        # if players rolled don't roll the same sum
        p1.dice = [5, 5]
        p2.dice = [2, 4]
        p1.die1, p1.die2 = 5, 5
        p2.die1, p2.die2 = 2, 4

        self.assertEqual(ref.checkSameSum(p1, p2), 0)

    def test_checkDoubles(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if only p1 rolls two 0's, p1 loses the whole game
        p1.die1, p1.die2 = 0, 0
        p2.die1, p2.die2 = 1, 2
        
        self.assertEqual(ref.checkDoubles(p1, p2), 1)
        self.assertEqual(p2.roundWins, 5)

        # if only p2 rolls two 0's, p2 loses the whole game
        p2.die1, p2.die2 = 0, 0

        p1.die1, p1.die2 = 1, 2 # reset from last assertion
        p2.roundWins = 0
        
        self.assertEqual(ref.checkDoubles(p1, p2), 1)
        self.assertEqual(p1.roundWins, 5)

        # if only p1 rolls two 10's, p1 wins the whole game
        p1.die1, p1.die2 = 10, 10
        p2.die1, p2.die2 = 1, 2
        
        self.assertEqual(ref.checkDoubles(p1, p2), 1)
        self.assertEqual(p1.roundWins, 5)

        # if only p2 rolls two 10's, p2 wins the whole game
        p2.die1, p2.die2 = 10, 10

        p1.die1, p1.die2 = 1, 2 # reset from last assertion
        p1.roundWins = 0
        
        self.assertEqual(ref.checkDoubles(p1, p2), 1)
        self.assertEqual(p2.roundWins, 5)

    def test_checkZero(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if no players rolled one zero
        p1.dice = [1, 1]
        p2.dice = [1, 2]
        p1.die1, p1.die2 = 1, 1
        p2.die1, p2.die2 = 1, 2

        self.assertEqual(ref.checkZero(p1, p2), 0)

        # if one or both players roll one zero
        p1.dice = [0, 1]
        p2.dice = [1, 2]
        p1.die1, p1.die2 = 0, 1
        p2.die1, p2.die2 = 1, 2

        self.assertEqual(ref.checkZero(p1, p2), 1)

        # if only p1 rolls one zero, p1 wins the round
        p1.roundWins = 0 # reset from last assertion

        ref.checkZero(p1, p2)
        self.assertEqual(p1.roundWins, 1)

        # if only p2 rolls one zero, p2 wins the round
        p2.dice = [0, 1]
        p1.dice = [1, 2]
        p2.die1, p2.die2 = 0, 1
        p1.die1, p1.die2 = 1, 2

        ref.checkZero(p1, p2)
        self.assertEqual(p2.roundWins, 1)

        # if p1 and p2 roll one zero and p1 has advantage, p1 wins the round
        p1.advantage = 1
        p2. advantage = 0
        p1.dice = [0, 1]
        p2.dice = [1, 0]
        p1.die1, p1.die2 = 0, 1
        p2.die1, p2.die2 = 1, 0
        p1.roundWins = 0 # reset from last assertion
        p2.roundWins = 0 # reset from last assertion

        ref.checkZero(p1, p2)
        self.assertEqual(p1.roundWins, 1)

        # if p1 and p2 roll one zero and p2 has advantage, p2 wins the round
        p1.advantage = 0
        p2.advantage = 1
        p1.roundWins = 0 # reset from last assertion
        p2.roundWins = 0 # reset from last assertion

        ref.checkZero(p1, p2)
        self.assertEqual(p2.roundWins, 1)

    def test_checkTen(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if no players rolled one ten
        p1.dice = [1, 1]
        p2.dice = [1, 2]
        p1.die1, p1.die2 = 1, 1
        p2.die1, p2.die2 = 1, 2

        self.assertEqual(ref.checkTen(p1, p2), 0)

        # if one or both players roll one ten
        p1.dice = [10, 1]
        p2.dice = [1, 2]
        p1.die1, p1.die2 = 10, 1
        p2.die1, p2.die2 = 1, 2

        self.assertEqual(ref.checkTen(p1, p2), 1)

        # if only p1 rolls one ten, p1 loses the round
        p2.roundWins = 0 # reset from last assertion

        ref.checkTen(p1, p2)
        self.assertEqual(p2.roundWins, 1)

        # if only p2 rolls one ten, p2 loses the round
        p2.dice = [10, 1]
        p1.dice = [1, 2]
        p2.die1, p2.die2 = 10, 1
        p1.die1, p1.die2 = 1, 2

        ref.checkTen(p1, p2)
        self.assertEqual(p1.roundWins, 1)

        # if p1 and p2 roll one ten and p1 has advantage, p1 wins the round
        p1.advantage = 1
        p2. advantage = 0
        p1.dice = [10, 1]
        p2.dice = [1, 10]
        p1.die1, p1.die2 = 10, 1
        p2.die1, p2.die2 = 1, 10
        p1.roundWins = 0 # reset from last assertion
        p2.roundWins = 0 # reset from last assertion

        ref.checkTen(p1, p2)
        self.assertEqual(p1.roundWins, 1)

        # if p1 and p2 roll one ten and p2 has advantage, p2 wins the round
        p1.advantage = 0
        p2. advantage = 1
        p1.roundWins = 0 # reset from last assertion
        p2.roundWins = 0 # reset from last assertion

        ref.checkTen(p1, p2)
        self.assertEqual(p2.roundWins, 1)

    def test_checkZeroTen(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if p1 rolls a 10 and a 0
        p1.dice = [10, 0]

        self.assertEqual(ref.checkZeroTen(p1, p2), 1)

        # if p2 rolls a 10 and a 0
        p2.dice = [10, 0]

        self.assertEqual(ref.checkZeroTen(p1, p2), 1)

        # if neither player rolls both a 10 and 0
        p1.dice = [1, 0]
        p2.dice = [10, 5]

        self.assertEqual(ref.checkZeroTen(p1, p2), 0)

    def test_checkDice(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        # if any player has both 10 and 0 (checkZeroTen)
        p1.dice = [10, 0]
        p2.dice = [10, 0]
        p1.die1, p1.die2 = 10, 0
        p2.die1, p2.die2 = 10, 0

        self.assertEqual(ref.checkDice(p1, p2), 1)

        # if both players rolled double 0's or 10's (checkSameSum)
        # if p2 has advantage
        p1.advantage = 0
        p2.advantage = 1
        p1.dice = [0, 0]
        p2.dice = [0, 0]
        p1.die1, p1.die2 = 0, 0
        p2.die1, p2.die2 = 0, 0

        self.assertEqual(ref.checkDice(p1, p2), -1)

        # if p2 has advantage (checkSameSum)
        p1.advantage = 1
        p2.advantage = 0
        p1.dice = [10, 10]
        p2.dice = [10, 10]
        p1.die1, p1.die2 = 10, 10
        p2.die1, p2.die2 = 10, 10

        self.assertEqual(ref.checkDice(p1, p2), -2)

        # if only p1 rolls double 10's (checkDoubles)
        p1.dice = [10, 10]
        p2.dice = [10, 2]
        p1.die1, p1.die2 = 10, 10
        p2.die1, p2.die2 = 10, 2
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 2)
        self.assertEqual(p1.roundWins, 5)
        self.assertEqual(ref.checkRoundWins(p1, p2), 1)

        # if only p2 rolls double 10's (checkDoubles)
        p1.dice = [10, 0]
        p2.dice = [10, 10]
        p1.die1, p1.die2 = 10, 0
        p2.die1, p2.die2 = 10, 10
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 2)
        self.assertEqual(p2.roundWins, 5)
        self.assertEqual(ref.checkRoundWins(p1, p2), 2)

        # if only p1 rolls double 0's (checkDoubles)
        p1.dice = [0, 0]
        p2.dice = [10, 2]
        p1.die1, p1.die2 = 0, 0
        p2.die1, p2.die2 = 10, 2
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 2)
        self.assertEqual(p2.roundWins, 5)
        self.assertEqual(ref.checkRoundWins(p1, p2), 2)

        # if only p2 rolls double 0's (checkDoubles)
        p1.dice = [10, 0]
        p2.dice = [0, 0]
        p1.die1, p1.die2 = 10, 0
        p2.die1, p2.die2 = 0, 0
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 2)
        self.assertEqual(p1.roundWins, 5)
        self.assertEqual(ref.checkRoundWins(p1, p2), 1)

        # if only p1 rolls a 0 (checkZero)
        p1.dice = [1, 0]
        p2.dice = [10, 1]
        p1.die1, p1.die2 = 1, 0
        p2.die1, p2.die2 = 10, 0
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 0)
        self.assertEqual(p1.roundWins, 1)

        # if only p2 rolls a 0 (checkZero)
        p1.dice = [5, 10]
        p2.dice = [0, 1]
        p1.die1, p1.die2 = 5, 10
        p2.die1, p2.die2 = 0, 1
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 0)
        self.assertEqual(p2.roundWins, 1)

        # if only p1 rolls a 10 (checkTen)
        p1.dice = [10, 1]
        p2.dice = [0, 1]
        p1.die1, p1.die2 = 10, 1
        p2.die1, p2.die2 = 0, 1
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 0)
        self.assertEqual(p2.roundWins, 1)

        # if only p2 rolls a 10 (checkTen)
        p1.dice = [0, 1]
        p2.dice = [10, 1]
        p1.die1, p1.die2 = 0, 1
        p2.die1, p2.die2 = 10, 1
        p1.roundWins = 0
        p2.roundWins = 0

        self.assertEqual(ref.checkDice(p1, p2), 0)
        self.assertEqual(p1.roundWins, 1)

        # if p1 and p2 roll the same sum w/o 0's or 10's (checkSameSum)
        p1.dice = [1, 3]
        p2.dice = [2, 2]
        p1.die1, p1.die2 = 1, 3
        p2.die1, p2.die2 = 2, 2

        self.assertEqual(ref.checkDice(p1, p2), 1)

        # if p1 rolls higher than p2
        p1.dice = [4, 1]
        p2.dice = [1, 1]
        p1.roundWins = 0
        p2.roundWins = 0

        ref.checkDice(p1, p2)
        self.assertEqual(p1.roundWins, 1)

        # if p2 rolls higher than p1
        p1.dice = [1, 1]
        p2.dice = [4, 1]
        p1.roundWins = 0
        p2.roundWins = 0

        ref.checkDice(p1, p2)
        self.assertEqual(p2.roundWins, 1)

    def test_checkRoundWins(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        p1.roundWins = 5

        self.assertEqual(ref.checkRoundWins(p1, p2), 0)

        p1.roundWins = 3
        p2.roundWins = 5

        self.assertEqual(ref.checkRoundWins(p1, p2), 2)

        p1.roundWins = 3
        p2.roundWins = 1

        self.assertEqual(ref.checkRoundWins(p1, p2), 0)

    def test_triggerGameOver(self):
        ref = Referee()
        p1 = Player("Player1")

        self.assertEqual(ref.triggerGameOver(p1), p1.name)

    def test_resetPlayer(self):
        ref = Referee()
        p1 = Player("Player1")

        p1.dice = [1, 2]
        p1.roundWins = 5

        ref.resetPlayer(p1)

        self.assertEqual(p1.dice, [])
        self.assertEqual(p1.roundWins, 0)

    def test_resetReferee(self):
        ref = Referee()

        ref.roundEnd = 1

        ref.resetReferee()

        self.assertEqual(ref.roundEnd, 0)

    def test_resetGame(self):
        ref = Referee()
        p1 = Player("Player1")
        p2 = Player("Player2")

        p1.dice = [1, 2]
        p1.roundWins = 5
        p2.dice = [2, 2]
        p2.roundWins = 1

        ref.roundEnd = 1

        ref.resetGame(p1, p2)

        self.assertEqual(p1.dice, [])
        self.assertEqual(p1.roundWins, 0)
        self.assertEqual(p2.dice, [])
        self.assertEqual(p2.roundWins, 0)
        self.assertEqual(ref.roundEnd, 0)


if __name__ == "__main__":
    unittest.main()