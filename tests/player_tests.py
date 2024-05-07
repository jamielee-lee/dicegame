# Jamie Lee
# CS 333
# Final Project
# Player Unit Tests

from player import Player
import unittest

class TestPlayerMethods(unittest.TestCase):
    def test_rollDice(self):
        player = Player("Jamie")

        player.rollDice()

        self.assertEqual(player.die1, player.dice[0])
        self.assertEqual(player.die2, player.dice[1])

if __name__ == "__main__":
    unittest.main()