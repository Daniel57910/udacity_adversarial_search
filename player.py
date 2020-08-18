class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.loc = {"X": None, "Y": None}
    
    def pos(self, x: int, y: int):
        self.loc["X"] = x
        self.loc["Y"] = y

    def actions_rows(self, board_size: int) -> dict:
        actions = {}
        x, y = self.loc["X"], self.loc["Y"]
        rows = [(x, i) for i in range(0, board_size)]
        cols = [(i, y) for i in range(0, board_size)]
        diags = self._diags(board_size)
        return set(rows + cols + diags)

    def _diags(self, board_size: int) -> dict:
        x, y = self.loc["X"], self.loc["Y"]
        diag = []
        while x < board_size-1 and y < board_size-1:
            x+=1
            y+=1
            diag.append((x, y))
      
        while x > 0 and y > 0:
            x-=1
            y-=1
            diag.append((x, y))
        
        return diag