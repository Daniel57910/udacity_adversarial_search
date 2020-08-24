import unittest
from player import Player
from gamestate import GameState
import pdb

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("!")
        self.player.pos(3,  0)
        self.game_state = GameState()

    def test_player_instantiation(self):
        self.assertEqual(self.player.loc["X"], 3)
        self.assertEqual(self.player.loc["Y"], 0)
    
    def test_get_actions_at_perimiter(self):
        legal_actions = self.player._all_actions()
        self.assertTrue(all(elem in legal_actions["horizontal"] + legal_actions["vertical"] for elem in [(3, 0), (3, 1), (3, 2), (3, 3)]))
    
    def test_get_positive_negative_diag(self):
        self.player.pos(3, 3)
        legal_actions = self.player._all_actions()
        diags = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (4, 2), (2, 4)]
        self.assertTrue(all(elem in legal_actions["diag"] + legal_actions["neg_diag"] for elem in diags))
    
    def test_get_all_moves_from_max_point(self):
        max_diags = [(0, 4), (4, 0), (4, 4), (0, 0)]
        self.player.pos(2, 2)
        legal_actions = self.player._all_actions()
        self.assertTrue(all(elem in legal_actions["diag"] + legal_actions["neg_diag"] for elem in max_diags))

      
    def test_get_all_legal_moves_with_gamestate(self):
        self.player.pos(2, 2)
        grid = self.game_state.grid
        grid[2][2] = "!"
        filled_values = [(1, 2), (2, 4), (3, 4), (4, 2)]
        grid = self._fill_values(grid, filled_values)
        self._print(grid)
        legal_values = [(3, 2), (2, 0), (2, 1), (2, 3), (0, 0), (1, 1), (3, 3), (4, 4), (0, 4), (1, 3), (3, 1), (4, 0)]
        legal_actions = self.player.identify_legal_actions(grid)
        print(legal_actions)
        self.assertTrue(all(a in legal_actions for a in legal_values))
      
    def test_get_all_moves_on_leftward_edge_constrained(self):
      self.player.pos(4, 0)
      grid = self.game_state.grid
      filled_values = [(0, 0), (0, 1), (0, 2), (0, 3), (3, 4), (1, 0), (2, 0), (3, 0), (4, 4)]
      legal_values = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 1), (4, 2), (4, 3)]
      grid[4][0] = "!"
      grid = self._fill_values(grid, filled_values)
      self._print(grid)
      legal_actions = self.player.identify_legal_actions(grid)
      print(legal_actions)
      self.assertTrue(all(a in legal_actions for a in legal_values))
    
    def test_get_boxed_in_case(self):
      grid = self.game_state.grid
      self.player.pos(2, 2)
      filled_values = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (1, 0), (2, 0), (3, 0)]
      grid[2][2] = "!"
      grid[2][1] = "!"
      grid[2][3] = "!"
      grid = self._fill_values(grid, filled_values)
      self._print(grid)
      legal_values = [(1, 2), (3, 2), (3, 3), (1, 1), (1, 3), (3, 1)]
      legal_actions = self.player.identify_legal_actions(grid)
      print(legal_actions)
      self.assertTrue(all(a in legal_actions for a in legal_values))

    def _fill_values(self, grid, filled_values):
      for (a, b) in filled_values: grid[a][b] = "X"
      return grid
    
    def _print(self, grid):
      print("\n")
      for g in grid: print(g)
