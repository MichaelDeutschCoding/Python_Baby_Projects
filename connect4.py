ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
  board = []
  for row in.....

  return board

def drop_piece(board, row, col, piece):
  pass

def valid_location(board, col):
  return board[5][col] == 0

def next_open_row(board, col):
  for r in range(ROW_COUNT):
    if board[r][col] == 0:
      return r

def printer(board):
  pass
  #for row in board[::-1]:
    print(row)
#print column numbers

board = create_board()
game_over = False
turn = 0

while not game_over:
  if turn == 0:
    col = int(input("Player One, choose a column: ")

    if valid_location(board, col):
              
