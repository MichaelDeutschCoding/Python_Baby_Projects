"""
Things to improve:

-add some more variety to comp_move3 in last {else} scenario.
        Could also go in a corner if we wanted.
-add sleep time
-define function to clear a new game


game specific variables:
    -board
    -full
    -c1, m1 etc.

universal variables:
    -corners
    -spaces



"""

from random import choice
from copy import deepcopy


def printer(board):
    print('', ' | '.join(board[0]))
    print('---|---|---')
    print('', ' | '.join(board[1]))
    print('---|---|---')
    print('', ' | '.join(board[2]))


corners = {(0,2), (2,0), (0,0), (2, 2)}
spaces = {(0, 0), (0, 1), (0, 2),
          (1, 0), (1, 1), (1, 2),
          (2, 0), (2, 1), (2, 2)}

def check_win(board):
    won = False
    
    for i in range(3):
        #check for vertical win
        if board[0][i] != '-' and board[0][i] == board[1][i] == board[2][i]:
            won = True
        #check for vertical win
        if board[i][0] != '-' and board[i][0] == board[i][1] == board[i][2]:
            won = True
    #check for diagonal win
    if board[1][1] != '-' and (board[0][0] == board[1][1] == board[2][2] or
    board[0][2] == board[1][1] == board[2][0]):
        won = True
    return won


def get_move():

    if check_win(board):
        print("Game over.")
        return
    while True:
        move = input("Where would you like to go? \
    (format your response as row number, column number): ")
        if move == 'Q':
            print("Goodbye.")
            return
        elif move.count(',') != 1:
            print('Invalid entry. Try again.')
            continue
        else:
            move = move.split(',')
            try:
                move[0] = int(move[0]) - 1
                move[1] = int(move[1]) - 1
            except:
                print("Error. Please try again.")
                continue
        move = tuple(move)
        if not move[0] in range(3) or not move[1] in range(3):
            print("That's out of range. Try again.")
            continue
        if move in full:
            print('That spot is already taken. Try again.')
            continue
        else:
            board[move[0]][move[1]] = 'O'
            full.add(move)
            printer(board)
            return move

def comp_move1():
    c1 = choice(list(corners))
    board[c1[0]][c1[1]] = 'X'
    print("Ok, it's my turn. Thinking where to go...")
    printer(board)
    full.add(c1)
    return c1

def comp_move2():

    # if m1 in corner, we go in either remaining corner
    if m1 in corners:
        c2 = choice(list(corners - full))

    # if m1 is middle, we go corner opposite c1
    elif m1 == (1, 1):
        c2 = (abs(c1[0] - 2), abs(c1[1] - 2))        
        
    # if user goes edge in same row, we go corner same columns as [c1]
    elif m1[0] == c1[0]:
        c2 = (abs(c1[0] - 2), c1[1])

    # if user goes edge in same column, we go corner same row as [c1]
    elif m1[1] == c1[1]:
        c2 = (c1[0], abs(c1[1] - 2))

    # if m1 is opposite edge, we can go either corner that's not opposite [c1]
    else:
        c2 = choice([(c1[0], abs(c1[1] - 2)), (abs(c1[0] - 2), c1[1])])

    board[c2[0]][c2[1]] = 'X'
    full.add(c2)
    printer(board)
    return c2

def comp_move3():

    # if player went in middle, then in edge -> comp must defend now. Will be tie.
    if m1 == (1, 1):
        if m2[0] == 1:                  #horizontal threat
            c3 = (1, abs(m2[1] -2))
        elif m2[1] == 1:                #vertical threat
            c3 = (abs(m2[0] - 2), 1)
        else:
            c3 = choice(list(corners - full))

    # check if player messed up
    elif c1[0] == c2[0] and (c1[0], 1) not in full: #horizontal win
        c3 = (c1[0], 1)
        print("I won")
    elif c1[1] == c2[1] and (1, c1[1]) not in full: #vertical win
        c3 = (1, c1[1])
        print("Oops, you made a mistake. I win")
    elif c2 == (abs(c1[0] - 2), abs(c1[1] - 2)) and (1, 1) not in full: # diagonal win
        c3 = (1, 1)
        print("that's embarassing...")

    elif m1 in corners:
        c3 = choice(list(corners - full))

    else:       #could improve this. There is also a move in a corner that would win.
        c3 = (1, 1)

    assert c3 not in full
    board[c3[0]][c3[1]] = 'X'
    full.add(c3)
    printer(board)
    return c3

def comp_move4():

    if (1, 1) not in full:
        c4 = (1, 1)
    elif len(corners - full) == 1:
        c4 = (corners - full).pop()
    else:
        remaining = spaces - full
        for space in remaining:
            testb = deepcopy(board)
            testb[space[0]][space[1]] = 'X'
            if check_win(testb):
                c4 = (space[0], space[1])
                break
        else:           # HUGE BUG!!!
            for spot in remaining:
                testc = deepcopy(board)
                testc[spot[0]][spot[1]] = 'O'
                if check_win(testc):
                    c4 = (spot[0], spot[1])
                    break
            else:
                c4 = choice(list(remaining))

    assert c4 not in full
    board[c4[0]][c4[1]] = 'X'
    full.add(c4)
    printer(board)
    return c4
        
def comp_move5():
    c5 = (spaces - full).pop()
    board[c5[0]][c5[1]] = 'X'
    print("Tie game.")
    printer(board)
    return c5
        

again = 'Y'
while again == 'Y':
    
    board = []
    for _ in range(3):
        board.append(['-'] * 3)
    full = set()

    print("Let's play Tic-Tac-Toe!")
    c1 = comp_move1()
    print("time for m1...")
    m1 = get_move()
    print("about to execute c2")
    c2 = comp_move2()
    print("now input for m2...")
    m2 = get_move()
    print("about to execute c3")
    c3 = comp_move3()
    if check_win(board):
        again = input("Type 'Y' if you want to play again: ")
        continue        
    print("getting input for m3...")
    m3 = get_move()
    if check_win(board):
        again = input("Type 'Y' if you want to play again: ")
        continue
    print("executing c4")
    c4 = comp_move4()
    if check_win(board):
        again = input("Type 'Y' if you want to play again: ")
        continue        
    print("getting m4 now")
    m4 = get_move()
    c5 = comp_move5()

else:
    print("Thanks for playing. Goodbye.")
