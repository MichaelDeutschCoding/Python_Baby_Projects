import random

class Score:
    score = 0

    def __init__(self, letter):
        self.name = "'Player " + letter + "' wins:"

    def __repr__(self):
        return self.name + ' ' + str(self.score)

    def plus_one(self):
        self.score +=1

x_win = Score('X')
o_win = Score('O')


def test1():
    "Just samplin' stuff, ya know."
    print("Hello, it's a me! Test1")
    print("o_win score:", o_win.score)
    def test2():
        print("Test2, reporting for duty, Sir.")
        print("I'ma print out x-score now:", x_win.score)
        o_win.plus_one()
    x_win.plus_one()
    test2()
    print("After calling 'test2':", o_win)
    def win_game():
        winner = random.choice([x_win, o_win])
        winner.plus_one()
        print("\tnow we got:\nX score:", x_win.score, "|| O score:", o_win.score)
    print("Calling the 'Win Game' function now:")
    win_game()
    print("job's done, boss.")

def status():
    print('\tSCORE:\n=======================================\n' + str(x_win), '|', o_win)


class Player:
    score = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name + ' has ' + str(self.score) + ' wins.'

player1 = Player(input("Player one, type your name. "))
player2 = Player(input("player two, type your name. "))

print(player1)
player1.score +=3
print("now we have " + str(player1))


            
