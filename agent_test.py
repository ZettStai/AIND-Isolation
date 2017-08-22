"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload
from minimaxhelpers import *


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        print ("Set up test")
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        print(self.game.to_string())

    def test_term(self):
        print("Term Test")
        print (terminal_test(self.game))

    def test_min(self):
        print ("Mini value test")
#        print(self.game.to_string())

    def test_h2(self):
        self.game.apply_move((2, 1))
        self.game.apply_move((6, 6))
        print ("Heuristic 2 test")
        print(self.game.to_string())
        x, y = self.game.get_player_location(self.player2)
        print("Player 2 position:")
        print (x,y)

if __name__ == '__main__':
    unittest.main()
