from player import Player
import copy
import pdb

class GameState:

    def __init__(self):
        self.player_count = -1
        self.board_size = 5
        self.grid = self._build_grid()
        self.players = [Player("X"), Player("!")]

    def actions(self):
        current_player = self.players[self.player_count]
        return current_player.identify_legal_actions(self.grid)

    def player(self):
        self.player_count += 1
        return self.player_count % 2
    
    def result(self, action):
        grid = copy.deepcopy(self.grid)
        y, x = action[0], action[1]
        allowed_actions = self.actions()
        if action not in allowed_actions:
            raise Exception("Space already occupied")
    
        grid[y][x] = self.players[self.player_count].symbol
        return grid

    def terminal_test(self):
        return not self.actions()
    
    def liberties(self, loc=None):
        """ Return a list of all open cells in the
        neighborhood of the specified location.  The list 
        should include all open spaces in a straight line
        along any row, column or diagonal from the current
        position. (Tokens CANNOT move through obstacles
        or blocked squares in queens Isolation.)
        
        Note: if loc is None, then return all empty cells
        on the board
        """
        # TODO: Finish this function!
        pass

    def _build_grid(self):
        return [["." for i in range(self.board_size)] for j in range(self.board_size)]
            

