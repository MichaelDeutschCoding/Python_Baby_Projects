from random import randrange, choice
from string import digits


#           TO DOs
# multiple ships
# various sized ships
# define class (ship)
# two players
# merge board coordinates into a tuple instead of separate components of row/col


def battleship():
  print()
  print("\t \t Let's Play Battleship!")
  print("You may press 'Q' at any time to quit.")
  sz = 5

  global again
  again = ""
  board = []
  for x in range(sz):
    board.append(["O"] * sz)

  def print_board(board):
    num = 65
    print("  " + " ".join(digits[1:sz + 1]))
    for row in board:
      print(chr(num), " ".join(row))
      num +=1

  print_board(board)


  ship_row = randrange(sz)
  ship_col = randrange(sz)

#hide a ship of length 3
  directions = []
  if ship_row >= 2:
    directions.append("up")
  if ship_row <= (sz - 3):
    directions.append("down")
  if ship_col >= 2:
    directions.append("left")
  if ship_col <= (sz - 3):
    directions.append("right")
  direction = choice(directions)
  
  print(directions)   ####
  print(direction)    ####

  if direction == "up":
    ship2_row = ship_row - 1
    ship3_row = ship_row - 2
    ship2_col = ship_col
    ship3_col = ship_col
  if direction == "down":
    ship2_row = ship_row + 1
    ship3_row = ship_row + 2
    ship2_col = ship_col
    ship3_col = ship_col
  else:
    pass
  if direction == "left":
    ship2_col = ship_col -1
    ship3_col = ship_col -2
    ship2_row = ship_row
    ship3_row = ship_row
  else:
    pass
  if direction == "right":
    ship2_col = ship_col + 1
    ship3_col = ship_col + 2
    ship2_row = ship_row
    ship3_row = ship_row
  else:
    pass



  print("ship row:", ship_row)
  print("ship col:", ship_col)
  print("ship2:", ship2_row, ship2_col)
  print(ship3_row, ship3_col)
  t = 0 #turn counter

  while True:
    print()
    print("\tTurn", t+1)
    guess = (input("Guess a Coordinate (letter first): ")).upper()
    if guess == "Q":
      print("Sorry to see you go.")
      return
    elif not len(guess) == 2 or not guess[0].isalpha() or not guess[1].isdigit():   #should it be If not len(guess) == 2
      print("Invalid Entry.")
      continue

    guess_row = ord(guess[0]) - 65
    guess_col = int(guess[1]) - 1

    if guess_row < 0 or guess_row > sz - 1 or guess_col < 0 or guess_col > sz -1:
      print("Oops, that's not even in the ocean!")
      continue
    elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "#":
      print("You've already guessed that spot.")
      continue
    if ((guess_row == ship_row and guess_col == ship_col) or
        (guess_row == ship2_row and guess_col == ship2_col) or 
        (guess_row == ship3_row and guess_col == ship3_col)):
      board[guess_row][guess_col] = "#"
      print("Hit!")
      print_board(board)
      if (board[ship_row][ship_col] == "#" and
          board[ship2_row][ship2_col] == "#" and
          board[ship3_row][ship3_col] == "#"):
        print("You sunk my battleship!!")
        print("Congratulations, you won!".center(75, '*'))
        break
      else:
        t +=1
        continue

    else:
      print("You missed my battleship.")
      board[guess_row][guess_col] = "X"
      t +=1
      print_board(board)
      
  again = input("Do you want to play again? type 'Y' for yes: ").upper()


def play():
  battleship()
  while again == "Y":
    print()
    battleship()
  else:
    print("Thanks for playing. Goodbye.")


play()
blah = input("MD")
        

  
