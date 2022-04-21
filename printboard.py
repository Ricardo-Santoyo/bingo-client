def printboard(board_list): # Prints board in easy to read layout.
  x = 0
  print(f'{"|B | |I | |N | |G | |O |":^24}')
  print('─'*24)
  for i in range(5):
    for i in range(5):
      print(f'|{(board_list[x][i]):^2s}|', end=' ')
    print('')
    print('─'*24)
    x+=1