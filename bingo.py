import send
import printboard
import check
import printmenu

game_code = None
board_code = None
board_list = []

def newgame(): # Starts a new game and returns the game code.
  message = "NG#"
  return send.message(message)

def getboard(gc): # Creates 2D array of the board and returns a board code.
  response = send.message(gc).split(',')
  board_code = response.pop(0)
  
  column = []
  for i in range(1, 26):
    column.append(response[i - 1])
    if i % 5 == 0:
      board_list.append(column)
      column = []
  board_list[2][2] = 'x'
  return board_code

def getstatus(gs): # Prints the current status of the game.
  response = send.message(gs).split(',')
  print(f'\nGame Code: {response[0]}')
  print(f'Board Code: {response[1]}')
  print(f'Number of Balls Drawn: {response[2]}')
  print(f'Status: {response[3]}\n')
  printboard.printboard(board_list)

def getball(gc, bc): # Gets the next ball from the server and returns the value.
  message = f'NB#{gc}#{bc}'
  response = send.message(message).split(',')
  return response[0]

def get_column(ball): # Returns the column number the ball would fall into.
  for i in range(4, -1, -1):
    if ball > str(i * 15):
      return i

def check_space(col, ball): # checks to see if space is equal to ball if so replaces it with x.
  for i in range(5):
    board_list[col][i] = 'x' if (board_list[col][i] == ball) else board_list[col][i]
  check.bingo(board_list)
  printboard.printboard(board_list)

def update_board(ball): # Updates the board with the ball given
  col = get_column(ball)
  check_space(col, ball)

def send_winner_info(BD): # Sends winner info to the server.
  message = f"WW#{game_code}#{board_code}#{BD}"
  send.message(message)

def quitgame(gc, bc): # Quits the game when the command is given.
    message = f'QG#ter{gc}#{bc}'
    response = send.message(message).split(',')
    return response[-1]

### Menu below ###
user_input = ''
while user_input < '6':

  match user_input:
    case "1":
      game_code = newgame()
    case "2": 
      gamecode = input(f'Enter game code:\n')
      game_code = gamecode
    case "3":
      board_code = getboard(f'GB#{game_code}')
    case "4":
      getstatus(f'GS#{game_code}')
    case "5":
      update_board(getball(game_code, board_code))

  printmenu.printmenu()
  user_input = input('\nEnter menu option here: ')
else:
  quitgame(game_code, board_code)