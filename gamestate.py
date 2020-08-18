from player import Player

class GameState:

    def __init__(self):
        self.player_count = -1
        self.board_size = 2
        self.grid = self._build_grid()
        self.player_1 = Player("X")
        self.player_2 = Player("!")

    
    def actions(self):
        """ Return a list of legal actions for the active player 
        
        You are free to choose any convention to represent actions,
        but one option is to represent actions by the (row, column)
        of the endpoint for the token. For example, if your token is
        in (0, 0), and your opponent is in (1, 0) then the legal
        actions could be encoded as (0, 1) and (0, 2).
        """
        # TODO: Finish this function!
        pass
    
    def player(self):
        self.player_count += 1
        return self.player_count % 2
        


    
    def result(self, action):
        """ Return a new state that results from applying the given
        action in the current state
        
        Hint: Check out the deepcopy module--do NOT modify the
        objects internal state in place
        """
        # TODO: Finish this function!
        pass
    
    def terminal_test(self):
        return not self.actions()
    
    def liberties(self, loc):
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
        grid = {}
        grid["values"] = [["." for i in range(self.board_size)] for j in range(self.board_size)]
        return grid
            

