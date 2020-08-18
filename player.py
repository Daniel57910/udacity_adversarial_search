class Player:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.loc = {"X": None, "Y": None}
    
    def pos(self, x: int, y: int):
        self.loc["X"] = x
        self.loc["Y"] = y

    def actions(self, board_size):
        return True
