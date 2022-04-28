def bingo(board): # checks the game board for bingo.
  if check_columns(board) or check_rows(board):
    print('Winner!')
  else:
    print('not yet.')

def check_columns(board): # checks all board columns for bingo
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

def check_rows(board):
  allrows = []
  row = []
  x = 0
  for i in range(5):
    for i in range(5):
      row.append(board[i][x])
      if i+1 == 5:
        allrows.append(row)
        row = []
    x+=1 
  all_equal = True
  for r in range(5):
    all_equal = True
    for space in allrows[r]:
      if space != 'x':
        all_equal = False
        break
    if all_equal:
      break
  return all_equal
