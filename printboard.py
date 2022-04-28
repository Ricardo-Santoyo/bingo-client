def printboard(board_list): # Prints board in easy to read layout.
  x = 0
  print(f'{"|B | |I | |N | |G | |O |":^24}')
  print('─'*24)
  for i in range(5):
    for i in range(5):
      print(f'|{(board_list[i][x]):^2s}|', end=' ')
    print('')
    print('─'*24)
    x+=1
  
def printmenu():
  print('MAIN MENU')
  print('Enter number for option')
  print('1 - New Game')
  print('2 - Join Existing Game')
  print('3 - Get Board')
  print('4 - Get Game Status')
  print('5 - Get Next Ball')
  print('6 - Quit Game & Client')