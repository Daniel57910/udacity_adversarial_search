def action_resolve(action_subset: list, coord: list, symbol: str) -> list:
  symbol_index = action_subset.index(symbol)
  action_length = len(action_subset)
  lower_bound, upper_bound = divide(action_subset, symbol_index, action_length)
  lower_coord_bound, upper_coord_bound = divide(coord, symbol_index, action_length)
  print(lower_bound, upper_bound)
  print(lower_coord_bound, upper_coord_bound)


def divide(arr, loc, length) -> list:
  return (arr[0:loc], arr[loc+1:length])