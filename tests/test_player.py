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
    
    def test_get_actions_at_perimiter(self):
        legal_actions = self.player.actions_rows(5)
        self.assertTrue(all(elem in legal_actions for elem in [(3, 0), (3, 1), (3, 2), (3, 3)]))
    
    def test_get_positive_negative_diag(self):
        self.player.pos(3, 3)
        legal_actions = self.player.actions_rows(5)
        diags = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (4, 2), (2, 4)]
        self.assertTrue(all(elem in legal_actions for elem in diags))
    
    def test_get_all_moves_from_max_point(self):
        max_diags = [(0, 4), (4, 0), (4, 4), (0, 0)]
        self.player.pos(2, 2)
        legal_actions = self.player.actions_rows(5)
        self.assertTrue(all(elem in legal_actions for elem in max_diags))


      
