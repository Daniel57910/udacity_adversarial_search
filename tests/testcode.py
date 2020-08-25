
from gamestate import *
import unittest

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gamestate = GameState()
    
    def test_n_n_grid_as_board_created(self):
        self.assertEqual(self.gamestate.grid[0][1], ".")

    def test_returns_correct_player(self):
        id_1, id_2 = self.gamestate.player(), self.gamestate.player()
        self.assertEqual(id_1, 0)
        self.assertEqual(id_2, 1)
        self.assertEqual(self.gamestate.player(), 0)
    
    def test_allow_legal_action_diagonal(self):
        filled_values = [(0, 0), (0, 1), (0, 2), (0, 3), (3, 4), (1, 0), (2, 0), (3, 0), (4, 4)]
        self.gamestate.grid = self._fill_values(self.gamestate.grid, filled_values)
        self.gamestate.grid[2][2] = "!"
        self.player_count = 1
        grid = self.gamestate.result((3, 1))
        self._print(grid)
        self.assertEqual(grid[3][1], "!")
    
    def test_legal_action_horizontal(self):
        filled_values = [(0, 0), (0, 1), (0, 2), (0, 3), (3, 4), (1, 0), (2, 0), (3, 0), (4, 4)]
        self.gamestate.grid = self._fill_values(self.gamestate.grid, filled_values)
        self.gamestate.grid[2][2] = "!"
        self.player_count = 1
        grid = self.gamestate.result((2, 4))
        self._print(grid)
        self.assertEqual(grid[2][4], "!")
    
    def test_raise_error_on_action_not_allowed(self):
        return True


    def _fill_values(self, grid, filled_values):
      for (a, b) in filled_values: grid[a][b] = "X"
      return grid
    
    def _print(self, grid):
      print("\n")
      for g in grid: print(g)



# print("Checking terminal test on an empty board...")
# if g.terminal_test() != False:
#     print("Failed\n Uh Oh! Your game marked an empty game state as terminal.")
# else:
#     print("Passed.")
    
# print("Checking liberties on an empty board...")
# p1_liberties = g.liberties(None)
# if len(p1_liberties) != 5:
#     print("Failed\n Uh oh! Your game did not return 5 empty " +
#           "cell locations as liberties on an empty board.")
# else:
#     print("Passed.")

# print("Getting legal moves for player 1...")
# p1_empty_moves = g.actions()
# print("Found {} legal moves.".format(len(p1_empty_moves or [])))

# print("Applying move {} for player 1...".format(p1_empty_moves[0]))
# g1 = g.result(p1_empty_moves[0])

# print("Getting legal moves for player 2...")
# p2_empty_moves = g1.actions()
# if len(p2_empty_moves) != 4:
#     print("Failed\n  Uh oh! Your game did not return the expected " +
#           "number of actions for player 2!")
# else:
#     print("Passed.")

# print("\nPlaying a full game")
# for _ in range(5):
#     if g.terminal_test(): break
#     g = g.result(g.actions()[0])

# print("Checking terminal test on a terminal board...")
# if g.terminal_test() != True:
#     print("Failed\n  Uh oh! Your game did not correctly evalute " +
#           "a terminal game state as terminal!")
# else:
#     print("Passed.")
