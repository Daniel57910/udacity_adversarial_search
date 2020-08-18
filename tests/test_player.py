import unittest
from player import Player
import pdb
class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("!")
        self.player.pos(3,  0)

    def test_player_instantiation(self):
        self.assertEqual(self.player.loc["X"], 3)
        self.assertEqual(self.player.loc["Y"], 0)
    
    def test_get_actions(self):
        legal_actions = self.player.actions(5)
        self.assertTrue(all(elem in legal_actions for elem in [(3, 0), (3, 1), (3, 2), (1, 0), (2, 0)]))

      
