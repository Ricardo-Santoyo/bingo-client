import send
import printboard
import check

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

  return board_code

def getstatus(gs): # Prints whether or not there is a winner.
  response = send.message(gs).split(',')
  if response[-1] == "W":
    print("Winner")
  else:
    print(board_list)
    print("No winner yet.")

def getball(gc, bc): # Gets the next ball from the server and returns the value.
  message = f'NB#{gc}#{bc}'
  response = send.message(message).split(',')
  return response[0]

def update_board(ball): # Updates the board with the ball given
  if ball > '60':
    check_space(4, ball)
    print('o')
  elif ball > '45':
    check_space(3, ball)
    print('g')
  elif ball > '30':
    check_space(2, ball)
    print('n')
  elif ball > '15':
    check_space(1, ball)
    print('i')
  else:
    check_space(0, ball)
    print('b')

def check_space(col, ball): # checks to see if space is equal to ball if so replaces it with x.
  for i in range(5):
    board_list[col][i] = 'x' if (board_list[col][i] == ball) else board_list[col][i]
    check.bingo(board_list)
  printboard.printboard(board_list)

def quitgame(gc, bc): # Quits the game when the command is given.
    message = f'QG#ter{gc}#{bc}'
    response = send.message(message).split(',')
    return response[-1]

### Menu below ###
user_input = ''

while user_input < '6':
  print('MAIN MENU')
  print('Enter number for option')
  print('1 - New Game')
  print('2 - Join Existing Game')
  print('3 - Get Board')
  print('4 - Get Game Status')
  print('5 - Get Next Ball')
  print('6 - Quit Game & Client')

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
  
  user_input = input()
else:
    quitgame(game_code, board_code)