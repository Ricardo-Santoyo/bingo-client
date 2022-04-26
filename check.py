def bingo(board): # checks the game board for bingo.
  if check_columns(board):
    print('Winner!')
  else:
    print('not yet.')

def check_columns(board): # checks all board columns for bingo.
  all_equal = True
  for col in range(5):
    all_equal = True
    for space in board[col]:
      if space != 'x':
        all_equal = False
        break
    if all_equal:
      break
  return all_equal

def check_diagonals(board): # checks the board diagonals for bingo.
  pass