"""
Game of Tic-Tac-Toe against a genius computer AI.
Computer is always 'X' and always goes first. (Player basically can't win.)

"""

from random import choice
from copy import deepcopy
from time import sleep

corners = {(0,2), (2,0), (0,0), (2, 2)}
spaces = {(0, 0), (0, 1), (0, 2),
          (1, 0), (1, 1), (1, 2),
          (2, 0), (2, 1), (2, 2)}

def check_win(grid):
    # takes in a 3x3 grid and returns a bool
    for i in range(3):
        #check for vertical win
        if grid[0][i] != '-' and grid[0][i] == grid[1][i] == grid[2][i]:
            return True
        #check for vertical win
        if grid[i][0] != '-' and grid[i][0] == grid[i][1] == grid[i][2]:
            return True
    #check for diagonal win
    if grid[1][1] != '-' and (grid[0][0] == grid[1][1] == grid[2][2] or
    grid[0][2] == grid[1][1] == grid[2][0]):
        return True
    return False

class Player:

    def __init__(self, name, team):
        self.name = name
        self.score = 0
        self.team = team

    def __repr__(self):
        return f"{self.name} has {self.score} wins and will now play {self.team}."

class Board:

    def __init__(self, team_x, team_o):
        self.grid =[]
        self.game_winner = None
        self.occupied = set()
        self.team_x = team_x
        self.team_o = team_o
        for _ in range(3):
            self.grid.append(['-'] * 3)

    def print_board (self):
        print()
        print('', ' | '.join(self.grid[0]))
        print('---|---|---')
        print('', ' | '.join(self.grid[1]))
        print('---|---|---')
        print('', ' | '.join(self.grid[2]))

    def validate_move(self, move):
        #takes in move as a string. Returns a tuple with the move's (x,y) coordinates
        if move.count(',') != 1:
            print("You must have one comma in your response.")
            return False
        
        move = move.split(',')
        try:   
            move[0] = int(move[0]) -1
            move[1] = int(move[1]) -1
        except ValueError:
            print("Must enter a number")
            return False
        move = tuple(move)
        if not move[0] in range(3) or not move[1] in range(3):
            print("That's out of range. Try again.")
            return False
        if move in self.occupied:
            print("That spot's already taken. Try again.")
            return False
        return move

    def get_move(self, Player):
        # asks user for a move. Once validated, writes it to the board.
        move = False
        print(f"Ok {Player.name}, your turn now.")
        while not move:
            move = input ("Where would you like to place an '" + Player.team + "'? (row num, col num): ")
            if move == "Q":
                return False
            move = self.validate_move(move)
        self.record_move(move, Player)
        return move

    def record_move(self, move, Player):
        # takes in move as a (x,y) tuple. Writes it to the board.
        self.grid[move[0]][move[1]] = Player.team
        self.occupied.add(move)
        self.print_board()
        if check_win(self.grid):
            print(f"Game over. {Player.name} wins!")
            self.game_winner= Player

    def comp_turn(self, comp, player):
        if len(self.occupied) < 2:
            self.c1 = self.comp_move1()
            self.record_move(self.c1, comp)
            if not self.game_winner:
                self.m1 = self.get_move(player)
        elif len(self.occupied) < 4:
            self.c2 = self.comp_move2()
            self.record_move(self.c2, comp)
            if not self.game_winner:
                self.m2 = self.get_move(player)
        elif len(self.occupied) < 6:
            self.c3 = self.comp_move3()
            self.record_move(self.c3, comp)
            if not self.game_winner:
                self.m3 = self.get_move(player)
        elif len(self.occupied) < 8:
            self.c4 = self.comp_move4()
            self.record_move(self.c4, comp)
            if not self.game_winner:
                self.get_move(player)
        else:
            self.record_move(self.comp_move5(), comp)

    def comp_move1(self):
        return choice(list(corners))
    
    def comp_move2(self):

        # if m1 in corner, we go in either remaining corner
        if self.m1 in corners:
            return choice(list(corners - self.occupied))

        # if m1 is middle, we go corner opposite c1
        if self.m1 == (1, 1):
            return (abs(self.c1[0] - 2), abs(self.c1[1] - 2))        
            
        # if user goes edge in same row, we go corner same columns as [c1]
        if self.m1[0] == self.c1[0]:
            return (abs(self.c1[0] - 2), self.c1[1])

        # if user goes edge in same column, we go corner same row as [c1]
        if self.m1[1] ==  self.c1[1]:
            return (self.c1[0], abs(self.c1[1] - 2))

        # if m1 is opposite edge, we can go either corner that's not opposite [c1]
        return choice([( self.c1[0], abs(self.c1[1] - 2)), (abs(self.c1[0] - 2), self.c1[1])])

    def comp_move3(self):

        # if player went in middle, then in edge -> comp must defend now. Will be tie.
        if self.m1 == (1, 1):
            if self.m2[0] == 1:                 #horizontal threat
                return (1, abs(self.m2[1] -2))
            elif self.m2[1] == 1:                    #vertical threat
                return (abs(self.m2[0] - 2), 1)

            return choice(list(corners - self.occupied))
 
        # check if player messed up
        elif self.c1[0] == self.c2[0] and (self.c1[0], 1) not in self.occupied: #horizontal win
            print("I won")
            return (self.c1[0], 1)
        elif self.c1[1] == self.c2[1] and (1, self.c1[1]) not in self.occupied: #vertical win
            print("Oops, you made a mistake. I win")
            return (1, self.c1[1])
        elif self.c2 == (abs(self.c1[0] - 2), abs(self.c1[1] - 2)) and (1, 1) not in self.occupied: # diagonal win
            print("that's embarassing...")
            return (1, 1)

        elif self.m1 in corners:
            return choice(list(corners - self.occupied))

        else:
            possible = [option for option in (corners - self.occupied) if (self.grid[1][option[1]] == '-' and self.grid[option[0]][1] == '-')]
            possible.append((1,1))
            return choice(possible)

    def comp_move4(self):

        if (1,1) not in self.occupied:
            return (1,1)

        remaining = spaces - self.occupied

        # Check if we can win in this move
        for location in remaining:
            tester = deepcopy(self.grid)
            tester[location[0]][location[1]] = 'X'
            if check_win(tester):
                return location

        # Check if THEY can win next move and we need to defend    
        for location in remaining:
            tester2 = deepcopy(self.grid)
            tester2[location[0]][location[1]] = 'O'
            if check_win(tester2):
                return location

        return choice(list(remaining))    

    def comp_move5(self):
        print("Well, this is pretty easy choice now!")
        return (spaces - self.occupied).pop()

def start_2player_game(x, o):
    game = Board(x, o)
    game.print_board()
    while not game.game_winner and len(game.occupied) < 9:
        if len(game.occupied) % 2 == 0:
            if not game.get_move(x):
                print(f"Quitter! {o.name} wins!")
                return o
        else:
            if not game.get_move(o):
                print(f"Quitter! {x.name} wins!")
                return x
    return game.game_winner

def main_2players():
    print("Welcome to Tic-Tac-Toe.\nTry to get three in a row!")
    player1 = Player(input("Player One, type in your name: "), "X")
    player2 = Player(input("Player Two, type in your name: "), "O")
    games_played = 0
    again = 'y'

    while again.startswith("y"):
        print("=" * 40)
        print(player1, player2, sep='\n')
        if games_played % 2 == 0:
            winner = start_2player_game(player1, player2)
        else:
            winner = start_2player_game(player2, player1)
        if winner:
            winner.score +=1
        else:
            print("Tie game.")
        games_played +=1
        player1.team, player2.team = player2.team, player1.team
        again = input("Do you want to play again? ").lower()
    print("=" * 8, "FINAL SCORE ", "=" * 8)
    print(f" {player1.name:>12} : {player1.score} ")
    print(f" {player2.name:>12} : {player2.score} ")

def start_game_comp(comp, player):
    game = Board(comp, player)
    while not game.game_winner and len(game.occupied) < 9:
        game.comp_turn(comp, player)
    return game.game_winner

def main_ai():
    comp = Player("GENIUS AI", 'X')
    player = Player(input("Enter your name: "), "O")
    again = 'y'
    while again.startswith('y'):
        winner = start_game_comp(comp, player)
        if winner:            winner.score +=1
        else:
            print("Tie game")
        print(comp, player, sep='\n')
        again = input("Do you want to play again? ").lower()


# main_2players()
main_ai()

