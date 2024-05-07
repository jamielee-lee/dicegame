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

        self.assertEqual(ref.checkSameSum(p1, p2), 1)

        # if players rolled don't roll the same sum
        p1.dice = [5, 5]
        p2.dice = [2, 4]

        self.assertEqual(ref.checkSameSum(p1, p2), 0)


if __name__ == "__main__":
    unittest.main()