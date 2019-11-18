#fix the quit bug
"""
def board_lines(x):
    " Draw lines for a square board of dimensions 'x' "
    for _ in range(x):
        print(' ---' * x)
        print('|   ' * x + "|")
    print(' ---' * x)
"""

class Player:
    score = 0

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __repr__(self):
        return self.name + ' has ' + str(self.score) + ' wins.'


def game(x, o):

    board = []
    for row in range(3):
        board.append(['-'] * 3)

    def printer(board):
        print()
        print(' | '.join(board[0]))
        print('--|---|--')
        print(' | '.join(board[1]))
        print('--|---|--')
        print(' | '.join(board[2]))

    def get_move(Player):
        print(f"\n\t {Player.name}, it's your turn.")
        while True:
            move = input("Where would you like to go? (row number, column number): ")
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
            if not move[0] in range(3) or not move[1] in range(3):
                print("That's out of range. Try again.")
                continue
            elif not board[move[0]][move[1]] == '-':
                print('That spot is already taken. Try again.')
                continue
            else:
                board[move[0]][move[1]] = Player.mark
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

    print("\nOk. Let's play Tic-Tac-Toe!")
    print(f"{x.name} will be 'X' for this game and go first. \
{o.name} will be 'O'.")
    printer(board)
    turn = 1

    while turn < 10:
        if turn % 2 == 1:
            get_move(x)
            if check_win(board):
                printer(board)
                print(f"Congratulations! {x.name} won the game!")
                x.score +=1
                return
            else:
                printer(board)
                turn += 1
                continue
        else:
            get_move(o)
            if check_win(board):
                printer(board)
                print(f"Congratulations! {o.name} won the game!")
                o.score +=1
                return
            else:
                printer(board)
                turn += 1
                continue
    else:
        print("Tie game. No winner.")


def main():
    print("Welcome to Tic-Tac-Toe.\nTry to get three in a row!")
    player1 = Player(input("Player One, type in your name: "), 'X')
    player2 = Player(input("Player Two, type in your name: "), 'O')

    gcount = 1
    
    again = 'y'
    while again == 'y':

        if gcount % 2 == 1:
            game(player1, player2)
        else:
            game(player2, player1)
        
        print('\tSCORE:\n=============================')
        print(player1, '||', player2)
        player1.mark, player2.mark = player2.mark, player1.mark
        gcount +=1
        again = input("Do you want to play again? (type 'y' for yes): ")
    else:
        print("Thanks for playing. Goodbye.")
    
        

main()    

