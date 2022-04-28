import send

def bingo(board, game_code, board_code): # checks the game board for bingo.
  if check_columns(board) or check_rows(board) or check_diagonals(board):
    print('\nWinner!\n')
  else:
    print('\nNot yet!\n')

def send_winner_info(BD, game_code, board_code): # Sends winner info to the server.
  message = f"WW#{game_code}#{board_code}#{BD}"
  send.message(message)

def check_columns(board): # checks all board columns for bingo.
  all_equal = True
  for col in range(5):
    all_equal = (f'C{col+1}')
    for space in board[col]:
      if space != 'x':
        all_equal = False
        break
    if all_equal:
      break
  return all_equal

def check_rows(board): # checks all board rows for bingo.
  all_equal = True
  for row in range(5):
    all_equal = (f'R{row+1}')
    for col in range(5):
      if board[col][row] != 'x':
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
      if loop == 0:
        all_equal = (f'DL')
      elif loop == 1:
        all_equal = (f'DR')
      break
  return all_equal