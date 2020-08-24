import pdb

def action_resolve(action_subset: list, coord: list, symbol: str) -> list:
  if not action_subset:
    return []

  if symbol not in action_subset:
    return []
  symbol_index = action_subset.index(symbol)
  action_length = len(action_subset)
  lower_bound, upper_bound = divide(action_subset, symbol_index, action_length)
  lower_coord, upper_coord = divide(coord, symbol_index, action_length)
  lower_index, upper_index = max(search(lower_bound), default=-1) , min(search(upper_bound), default=len(upper_coord) + 1)
  return lower_coord[lower_index+1: len(lower_coord)] + upper_coord[0: upper_index]


def divide(arr, loc, length) -> list:
  return (arr[0:loc], arr[loc+1:length])

def search(arr) -> list:
  return [i for i, x in enumerate(arr) if x != "."]

