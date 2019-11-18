from random import choice

active = set()

def reset_board():
    put_down_piece((3,4), 'X')
    put_down_piece((4,3), 'X')
    put_down_piece((4,4), 'O')
    put_down_piece((3,3), 'O')


board = []
for _ in range(8):
    board.append(['-']* 8)

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
    # Returns list of (x,y) tuples
    x,y = location
    return [
        (x, y-1), (x+1, y-1), (x+1, y),
        (x+1, y+1),  (x, y+1), (x-1, y+1),
        (x-1, y), (x-1, y-1)
    ]

def update_active(location):
    for spot in neighbors(location):
        try:
            if board[spot[0]][spot[1]] == '-':
                board[spot[0]][spot[1]] = '~'
                active.add((spot))
        except IndexError:
            continue

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
    while True:
        try:
            if peek(direction(start)) != opp:
                break
            else:
                start = direction(start)
                sandwiched.append(start)
        except IndexError:
            break
    if peek(direction(start)) == team:
        return sandwiched
    else:
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


put_down_piece((3,4), 'X')
put_down_piece((4,3), 'X')
put_down_piece((3,3), 'X')
put_down_piece((3,5), 'X')
put_down_piece((4,4), 'O')
put_down_piece((4,5), 'O')
put_down_piece((4,2), 'O')

display()

comp_turn('O')
comp_turn('X')
comp_turn('O')
