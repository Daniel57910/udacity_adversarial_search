import pdb

def action_resolve(action_subset: list, coord: list, symbol: str) -> list:
  symbol_index = action_subset.index(symbol)
  action_length = len(action_subset)
  lower_bound, upper_bound = divide(action_subset, symbol_index, action_length)
  lower_coord_bound, upper_coord_bound = divide(coord, symbol_index, action_length)
  lower_index, upper_index = max(search(lower_bound)) , min(search(upper_bound))
  pdb.set_trace()
  return coord[lower_index:symbol_index- 1] + coord[symbol_index+1: upper_index +symbol_index+1]

def divide(arr, loc, length) -> list:
  return (arr[0:loc], arr[loc+1:length])

def search(arr) -> list:
  print(arr)
  return [i for i, x in enumerate(arr) if x != "."]

