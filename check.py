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
  all_equal = True
  for loop in range(2):
    all_equal = True
    for i in range(5):
      space = 4 - i if (loop == 1) else i
      if board[i][space] != 'x':
        all_equal = False
        break
    if all_equal:
      break
  return all_equal