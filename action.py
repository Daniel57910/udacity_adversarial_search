import copy
from action_resolve import action_resolve
class Action:

    def __init__(self, coord: tuple, grid: list, board_size=5):
        self.grid = grid
        self.coord = coord
        self.board_size = board_size
        self.basis = ["horizontal", "vertical", "diag", "neg_diag"]
    
    
    def valid_actions(self):
        possible_actions = self._all_actions()
        subsets = []
        for base in self.basis:
          subset = [self.grid[x][y] for (x, y) in possible_actions[base]]
          subsets.extend(action_resolve(subset, possible_actions[base], self.symbol))
        
        return subsets
    
    def liberties(self):
        liberties = []
        possible_actions = self._all_actions()
        for basis in self.basis:
            liberties.extend((y, x) for (y, x) in possible_actions[basis] if self.grid[y][x] == ".")
        return set(liberties)

    def _all_actions(self) -> dict:
        actions = {}
        x, y = self.coord[1], self.coord[0]
        actions["horizontal"] = [(x, i) for i in range(0, self.board_size)]
        actions["vertical"] = [(i, y) for i in range(0, self.board_size)]
        actions["diag"], actions["neg_diag"] = self._diags(x, y)
        return actions

    def _diags(self, x: int, y: int) -> dict:
        x_pos, y_neg = copy.deepcopy(x), copy.deepcopy(y)
        diag = []
        neg_diag = []

        # later: refactor to invert eg (0, 5) -> (5, 0) on negative gradient
        while x < self.board_size-1 and y < self.board_size-1:
            x+=1
            y+=1
            diag.append((x, y))
      
        while x > 0 and y > 0:
            x-=1
            y-=1
            diag.append((x, y))

        while x_pos > 0 and y_neg < self.board_size-1:
            x_pos-=1
            y_neg+=1
            neg_diag.append((x_pos, y_neg))
        
        while x_pos < self.board_size-1 and y_neg > 0:
            x_pos += 1
            y_neg -=1
            neg_diag.append((x_pos, y_neg))
        
        return diag, neg_diag
