import copy
import time
from action_resolve import action_resolve
import pdb
class Player:
    def __init__(self, symbol: str, board_size=5):
        self.symbol = symbol
        self.loc = {"X": None, "Y": None}
        self.board_size = board_size
        self.basis = ["horizontal", "vertical", "diag", "neg_diag"]
    
    def pos(self, x: int, y: int):
        self.loc["X"] = x
        self.loc["Y"] = y

    def identify_legal_actions(self, grid: list):
        possible_actions = self._all_actions()
        vertical_subset = [grid[x][y] for (x, y) in possible_actions["vertical"]]
        horizontal_subset = [grid[x][y] for (x, y) in possible_actions["horizontal"]]
        diag_subset = [grid[x][y] for (x, y) in possible_actions["diag"]]
        neg_diag_subset = [grid[x][y] for (x, y) in possible_actions["neg_diag"]]
        legal_vertical = action_resolve(vertical_subset, possible_actions["vertical"], self.symbol)
        legal_horizontal = action_resolve(horizontal_subset, possible_actions["horizontal"], self.symbol)
        legal_diag = action_resolve(diag_subset, possible_actions["diag"], self.symbol)
        legal_neg_diag = action_resolve(neg_diag_subset, possible_actions["neg_diag"], self.symbol)
        return legal_vertical + legal_horizontal + legal_diag + legal_neg_diag

    def _all_actions(self) -> dict:
        actions = {}
        x, y = self.loc["X"], self.loc["Y"]
        actions["horizontal"] = [(x, i) for i in range(0, self.board_size)]
        actions["vertical"] = [(i, y) for i in range(0, self.board_size)]
        actions["diag"], actions["neg_diag"] = self._diags()
        return actions

    def _diags(self) -> dict:
        x, y = self.loc["X"], self.loc["Y"]
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


