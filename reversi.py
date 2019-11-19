from random import choice

max_x = 8
max_y = 8

active = set()
board = []
for _ in range(max_y):
    board.append(['-']* max_x)

def blank_board():
    for r in range(max_y):
        for c in range(max_x):
            board[r][c] = '-'
    active.clear()

def reset_board():
    # active = set()
    # board = []

    put_down_piece((3,4), 'X')
    put_down_piece((4,3), 'X')
    put_down_piece((4,4), 'O')
    put_down_piece((3,3), 'O')
    # return board


def display():
    for row in board:
        print(' '.join(row))

def peek(t):
    # Takes a (x,y) tuple and returns that location on the board
    return board[t[0]][t[1]]

def put_down_piece(location, team):
    x, y = location
    board[x][y] = team
    update_active(location)
    active.discard(location)

def neighbors(location):
    y, x = location
    return [(y2, x2) for x2 in range(x-1, x+2)
        for y2 in range(y-1, y+2)
            if (0 <= x <= max_x  and
            0 <= y <= max_y and
            (x != x2 or y != y2) and
            (0 <= x2 < max_x) and
            (0 <= y2 < max_y))]


def update_active(location):
    for spot in neighbors(location):
        if board[spot[0]][spot[1]] == '-':
            board[spot[0]][spot[1]] = '~'
            active.add((spot))

def find_all_possible_moves(team):
    possible = {}

    for location in active:
        results = checkspace(location, team)
        if results:
            possible[location] = results
    return possible

def comp_turn(team):
    possible = find_all_possible_moves(team)
    new_piece = max(possible.items(), key=lambda x: len(x[1]))[0]
    print("I went in:", new_piece, possible[new_piece])
    put_down_piece((new_piece), "*")
    display()
    print("=" * 15)
    put_down_piece((new_piece), team)
    for loc in possible[new_piece]:
        put_down_piece((loc), team)
    display()


def checkspace(loc, team):
    flip = []
    opp = 'O' if team == 'X' else 'X'

    for direction in directions:
        flip += check_dir(loc, direction, team, opp)
    return flip

def check_dir(start, direction, team, opp):
    # returns list of sandwich spaces in that single direction

    sandwiched = []
    try:
        while True:
            if peek(direction(start)) != opp:
                break
            else:
                start = direction(start)
                if start[0] == 0 or start[1] == 0:
                    return []
                sandwiched.append(start)

        if peek(direction(start)) == team:
            return sandwiched
        else:
            return []
    except IndexError:
        return []
        
directions = [
    lambda l : (l[0], l[1]-1),
    lambda l : (l[0]+1, l[1]-1),
    lambda l : (l[0]+1, l[1]),
    lambda l : (l[0]+1, l[1]+1),
    lambda l : (l[0], l[1]+1), 
    lambda l : (l[0]-1, l[1]+1),
    lambda l : (l[0]-1, l[1]), 
    lambda l : (l[0]-1, l[1]-1)
]

"""
put_down_piece((3,4), 'X')
put_down_piece((4,3), 'X')
put_down_piece((3,3), 'X')
put_down_piece((3,5), 'X')
put_down_piece((4,4), 'O')
put_down_piece((4,5), 'O')
put_down_piece((4,2), 'O')

display()
"""
reset_board()

for _ in range(12):
    comp_turn('O')
    comp_turn('X')
