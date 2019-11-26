from random import randrange, choice
from string import digits

class Ship:
  "The five ships that will be hidden in the Battleship board."
  
  def __init__(self, name, length):
    self.name = name
    self.length = length
    self.hits = 0
    self.remaining = self.length - self.hits
    self.sunk = False
    self.ship_loc = []
    
  def get_hit(self):
    if self.remaining > 1:
      self.hits +=1
      self.remaining -=1
      print("Hit!! You nailed my %s, it can only take another %s shots!" % (self.name, self.remaining))
    elif self.remaining == 1:
      self.hits +=1
      self.remaining -=1
      self.sunk = True
      print("~~ Hit and Sunk!!! You sunk my %s!! ~~" % self.name)
    else:
      print("You've already sunk %s." % self.name)    

  def hide(self, sz, existing):
    while True:
      self.ship_loc = []
      main = (randrange(sz), randrange(sz))
      ori = choice('up down left right'.split())
      if ori == 'up':
        for i in range(self.length):
          self.ship_loc.append((main[0]-i, main[1]))
      if ori == 'down':
        for i in range(self.length):
          self.ship_loc.append((main[0]+i, main[1]))
      if ori == 'left':
        for i in range(self.length):
          self.ship_loc.append((main[0], main[1] - i))
      if ori == 'right':
        for i in range(self.length):
          self.ship_loc.append((main[0], main[1]+i))
      in_ocean = all(i < sz and i >= 0 for i in [item for sublist in self.ship_loc for item in sublist])
      if not in_ocean:
        continue
      if not set(self.ship_loc).isdisjoint(existing):
        continue
      else:
        return self.ship_loc
      
  def describe(self):
    if self.sunk:
      print(" ~", self.name, "has already been sunk.")
    else:
      print("%s is of length %s. It's been hit %s times and has %s shots remaining."
          % (self.name, self.length, self.hits, self.remaining))

carrier = Ship("Aircraft Carrier", 5)
bship = Ship('Battleship', 4)
cruiser = Ship('Cruiser', 3)
sub = Ship('Submarine', 3)
patrol = Ship('Patrol Boat', 2)
fleet = [carrier, bship, cruiser, sub, patrol]

sz = 9
again = ""

def populate():
  locations = []
  
  carrier.hide(sz, locations)
  locations.extend(carrier.ship_loc)

  bship.hide(sz, locations)
  locations.extend(bship.ship_loc)

  cruiser.hide(sz, locations)
  locations.extend(cruiser.ship_loc)

  sub.hide(sz, locations)
  locations.extend(sub.ship_loc)

  patrol.hide(sz, locations)
  locations.extend(patrol.ship_loc)

  return locations

def printer(board):
  num = 65
  print("  " + " ".join(digits[1:sz + 1]))
  for row in board:
    print(chr(num), " ".join(row))
    num +=1

def battleship():
  board = []
  for x in range(sz):
    board.append(["O"] * sz)
  locations = populate()
  print("\n \t ~~~ Let's Play Battleship! ~~~")
  print("You may type 'Q' at any time to quit. Type 'status' for a status report.")
  printer(board)

  t = 0
  while t < 50:
    print("\n\tTurn", t+1)
    guess = input("Fire at a spot on the board (letter first): ").upper()
    if guess == "Q":
      print("Sorry to see you go.")
      return
    elif guess == "ADMIN":
      print(locations)
      continue
    elif guess == "STATUS":
      print("\n\tSTATUS REPORT:")
      for item in fleet:
        item.describe()
      continue
    elif not len(guess) == 2 or not guess[0].isalpha() or not guess[1].isdigit():
      print("Invalid entry.")
      continue
    guess = (ord(guess[0]) - 65, int(guess[1]) - 1)
    if guess[0] not in range(sz) or guess[1] not in range(sz):
      print("Oops, that's not even in the ocean!")
      continue
    if board[guess[0]][guess[1]] != "O":
      print("You've already guessed that spot.")
      continue

    if guess in locations:
      if guess in carrier.ship_loc:
        carrier.get_hit()
      elif guess in bship.ship_loc:
        bship.get_hit()
      elif guess in cruiser.ship_loc:
        cruiser.get_hit()
      elif guess in sub.ship_loc:
        sub.get_hit()
      else:
        patrol.get_hit()
      board[guess[0]][guess[1]] = "#"
      printer(board)
      t +=1      

    else:
      print("Miss.")
      board[guess[0]][guess[1]] = "x"
      printer(board)
      t +=1

    if all([carrier.sunk, bship.sunk, cruiser.sunk, sub.sunk, patrol.sunk]):
      print("Congratulations! You won!")
      return
  else:
    print("Sorry. You lost.")
    

    
      
      
    
    

