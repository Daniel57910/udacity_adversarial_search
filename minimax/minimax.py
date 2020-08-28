
from minimax_helpers import *
import pdb

def minimax_decision(gameState):
    return next(a for a in gameState.actions() if min_value(gameState.result(a)) > 0)
