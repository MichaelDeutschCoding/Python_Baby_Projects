
"""
def board_lines(x):
    " Draw lines for a square board of dimensions 'x' "
    for _ in range(x):
        print(' ---' * x)
        print('|   ' * x + "|")
    print(' ---' * x)
"""

class Score:
    score = 0

    def __init__(self, letter):
        self.name = "'Player " + letter + "' wins:"

    def __repr__(self):
        return self.name + ' ' + str(self.score)

x_win = Score('X')
o_win = Score('O')


def game():

    board = []
    for row in range(3):
        board.append(['-'] * 3)

    def printer(board):
        for row in board:
            print(row)

    def get_move(player):
        print(f"\n\tPlayer {player}, it's your turn.")
        while True:
            move = input("Where would you like to go? \
(format your response as row number, column number): ")
            if move == 'Q':
                print("Goodbye.")
                return
            elif move.count(',') != 1:
                print('Your answer must contain exactly one comma. Try again.')
                continue
            else:
                move = move.split(',')
                try:
                    move[0] = int(move[0]) - 1
                    move[1] = int(move[1]) - 1
                except:
                    print("Error. Please try again.")
                    continue
            if not move[0] in range(3) or not move[1] in range(3):
                print("That's out of range. Try again.")
                continue
            elif not board[move[0]][move[1]] == '-':
                print('That spot is already taken. Try again.')
                continue
            else:
                board[move[0]][move[1]] = player
                break

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

    print("Welcome. Let's play Tic-Tac-Toe!")
    printer(board)
    turn = 1

    while turn < 10:
        if turn % 2 == 1:
            get_move('X')
            if check_win(board):
                printer(board)
                print("Congratulations! Player 'X' won the game!")
                x_win.score +=1
                return
            else:
                printer(board)
                turn += 1
                continue
        else:
            get_move('O')
            if check_win(board):
                printer(board)
                print("Congratulations! Player 'O' won the game!")
                o_win.score +=1
                return
            else:
                printer(board)
                turn += 1
                continue
    else:
        print("Tie game. No winner.")


def main():
    again = 'y'
    while again == 'y':
        game()
        print('\tSCORE:\n=============================')
        print(x_win, '||', o_win)
        again = input("Do you want to play again? (type 'y' for yes): ")
    
main()