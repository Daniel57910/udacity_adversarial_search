class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.loc = {"X": None, "Y": None}
    
    def pos(self, x: int, y: int):
        self.loc["X"] = x
        self.loc["Y"] = y

    def actions(self, board_size: int) -> dict:
        actions = {}
        x, y = self.loc["X"], self.loc["Y"]
        rows = [(x, i) for i in range(0, board_size)]
        cols = [(i, y) for i in range(0, board_size)]
        return set(rows + cols)
