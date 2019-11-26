from random import randrange, choice
from string import digits


#           TO DOs
# various sized ships
# define class (ship)
# two players


def battleship():
  print()
  print("\t \t ~~~ Let's Play Battleship! ~~~")
  print("You may type 'Q' at any time to quit.")

  sz = input("What size board would you like to play? Enter a number between 5 - 9: ")
  if not sz.isdigit():
    sz = 5
  else:
    sz = int(sz)
  if sz < 5 or sz > 9:
    sz = 5
  
  num_ships = input("How many ships? ")
  if not num_ships.isdigit():
    num_ships = 5
  else:
    num_ships = int(num_ships)
  if num_ships < 3 or num_ships > (sz**2 - 4):
    num_ships = 5

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

# hiding 'big_ship' of length 3
  ship_row = randrange(sz)
  ship_col = randrange(sz)
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

  if direction == "up":
    ship2_row = ship_row - 1
    ship3_row = ship_row - 2
    ship2_col = ship3_col = ship_col
  if direction == "down":
    ship2_row = ship_row + 1
    ship3_row = ship_row + 2
    ship2_col = ship3_col = ship_col
  if direction == "left":
    ship2_col = ship_col -1
    ship3_col = ship_col -2
    ship2_row = ship3_row = ship_row
  if direction == "right":
    ship2_col = ship_col + 1
    ship3_col = ship_col + 2
    ship2_row = ship3_row = ship_row

  big_ship = [(ship_row, ship_col),(ship2_row, ship2_col),(ship3_row, ship3_col)] 

  def fill_ocean(num_ships, sz, existing):
    locations = set(existing)
    while len(locations) < num_ships + 3:
      locations.add((randrange(sz), randrange(sz)))
    return list(locations)

  locations = fill_ocean(num_ships, sz, big_ship)
#  print(locations)

  print_board(board)
  t = 0 #turn counter
  big_hits = 0
  remaining = len(locations)

  while True:
    print()
    print("\tTurn", t+1)
    print("\tShips remaining:", remaining)
    guess = (input("Guess a Coordinate (letter first): ")).upper()
    if guess == "Q":
      print("Sorry to see you go.")
      return
    elif not len(guess) == 2 or not guess[0].isalpha() or not guess[1].isdigit():   
      print("Invalid Entry.")
      continue

    guess_row = ord(guess[0]) - 65
    guess_col = int(guess[1]) - 1
    guess = (guess_row, guess_col)
    if (guess[0] < 0 or
        guess[0] > sz - 1 or
        guess[1] < 0 or
        guess[1] > sz -1):
      print("Oops, that's not even in the ocean!")
      continue

    if board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "#":
      print("You've already guessed that spot.")
      continue
    if guess in locations:
      t += 1
      board[guess[0]][guess[1]] = "#"
      print("Hit!")
      if guess in big_ship:
        big_hits += 1
        if big_hits == 3:
          print("~~~You sunk my battleship!!~~~")
        else:
          print("You hit my battleship!")
      else:
        print("~You sunk my patrol boat!!~")
      print_board(board)
      remaining = len(locations) - sum(x.count("#") for x in board)
      if remaining == 0:
        print("Congratulations, you won!".center(75, '*'))
        break
      else:
        continue

    else:
      print("Miss.")
      board[guess_row][guess_col] = "X"
      t +=1
      print()
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
        

  
