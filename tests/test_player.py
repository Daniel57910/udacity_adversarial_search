import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def test_player_instantiation(self):
        player = Player("!")
        player.pos(3,  0)
        self.assertEqual(player.loc["X"], 3)
        self.assertEqual(player.loc["Y"], 0)