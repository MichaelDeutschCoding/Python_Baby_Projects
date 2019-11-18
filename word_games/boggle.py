import random
from time import sleep
from collections import Counter

"""TODO:
-add sleep

from string import ascii_uppercase
letter_weights = [12,5,6,6,15,5,5,7,12,4,4,7,7,6,12,5,2,7,10,9,11,3,4,1,4,2]

def rand_grid():
    grid = [['*'] * 6]
    for i in range(1,5):
        grid.append(random.choices(ascii_uppercase, weights= letter_weights, k=4))
        grid[i].insert(0, '*')
        grid[i].append('*')
    grid.append(['*'] *6)
    return grid

grid = [['*', '*', '*', '*', '*', '*'],
['*', 'E', 'QU', 'I', 'E', '*'],
['*', 'I', 'P', 'L', 'T', '*'],
['*', 'F', 'M', 'O', 'M', '*'],
['*', 'C', 'D', 'W', 'O', '*'],
['*', '*', '*', '*', '*', '*']]

grid = [['*', '*', '*', '*', '*', '*'],
['*', 'S', 'N', 'X', 'P', '*'],
['*', 'P', 'A', 'X', 'L', '*'],
['*', 'A', 'E', 'E', 'QU', '*'],
['*', 'N', 'I', 'S', 'H', '*'],
['*', '*', '*', '*', '*', '*']]
"""

dice =[['A', 'A', 'E', 'E', 'G', 'N'], ['A', 'B', 'B', 'J', 'O', 'O'], ['A', 'C', 'H', 'O', 'P', 'S'], ['A', 'F', 'F', 'K', 'P', 'S'], ['A', 'O', 'O', 'T', 'T', 'W'], ['C', 'I', 'M', 'O', 'T', 'U'], ['D', 'E', 'I', 'L', 'R', 'X'], ['D', 'E', 'L', 'R', 'V', 'Y'], ['D', 'I', 'S', 'T', 'T', 'Y'], ['E', 'E', 'G', 'H', 'N', 'W'], ['E', 'E', 'I', 'N', 'S', 'U'], ['E', 'H', 'R', 'T', 'V', 'W'], ['E', 'I', 'O', 'S', 'S', 'T'], ['E', 'L', 'R', 'T', 'T', 'Y'], ['H', 'I', 'M', 'N', 'U', 'Qu'], ['H', 'L', 'N', 'N', 'R', 'Z']]

def boggle_grid():
    grid = [['*'] * 4]
    selection = [random.choice(die) for die in dice]
    random.shuffle(selection)
    for i in range(0, len(selection), 4):
        grid.append(selection[i:i+4])
    for row in grid:
        row.insert(0, '*')
        row.append('*')
    grid.append(['*'] * 6)
    return grid

valid = []
grid = boggle_grid()
score = 0
points = {3:1, 4:1, 5:2, 6:3, 7:5, 8:11, 9:11, 10:11}

def display():
    if valid:
        print('Score:', score, '   Already guessed:', ', '.join(valid))
    print('\t ', '-' * 14, sep = '')
    for row in grid[1:5]:
        print('\t |',f"{row[1]:<2} {row[2]:<2} {row[3]:<2} {row[4]:<2}|")
    print('\t ', '-' * 14, sep = '')

def find_word(guess):
    stack = []
    word = list(guess)
    for i in range(len(word)-1):
        if word[i] == 'Q' and word[i+1] == 'U':
            word[i:i+2] = ['QU']
    for r in range(1,5):
        for c in range(1,5):
            if grid[r][c] == word[0]:
                stack.append((r, c, 0, [(r, c)]))
    while stack:
        r, c, i, v = stack.pop()
        if i+1 == len(word):
            #valid.append(guess)
            return True
        visited = list(v)
        search(r, c, i, visited, word, stack)

    return False

def search(r, c, i, visited, word, stack):
    #print(f"Searching for {word[i+1]} from ({r}, {c}). Already visited: {visited} len stack: {len(stack)}")
    for row, col in (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1):
        if grid[row][col] == word[i+1] and (row, col) not in visited:
            stack.append((row, col, i+1, visited + [(row, col)]))

with open('boggle_words.txt') as f:
    acceptable = set(f.read().splitlines())

D = Counter([letter for die in grid for letter in die])

def let_count(word):
    word = list(word)
    for i in range(len(word)-1):
        if word[i] == 'Q' and word[i+1] == 'U':
            word[i:i+2] = ['QU']
    for letter in set(word):
        if word.count(letter) > D[letter]:
            return False
    return True

maybe = [w for w in acceptable if let_count(w)]
found = [word for word in maybe if find_word(word)]

def play():
    print("Let's play BOGGLE!")
    print("Shaking the board.")
    global score
    #sleep(2)
    print(f"Here are your letters. I've found {len(found)} words in this board.")
    display()
    while True:
        guess = input("Type a word that can be made from the letters in the board: ").upper()
        print()
        if guess == '!Q':
            print('Goodbye')
            break
        elif guess == '!B':
            display()
            
        elif guess == '!CHEAT':
            print(found)
            
        elif guess == '!BEST':
            best = sum([points[len(w)] for w in found])
            print(f"Number of valid words: {len(found)}, for a total score of: {best}")

        elif len(guess) < 3:
            print('Must be 3 letters or more.')
            
        elif guess not in acceptable:
            print('Not a valid word.')
            
        elif guess in valid:
            print("You've already guessed that word.")
            
        elif guess not in found:
            print("That word can't be made with the available letters.")
            
        else:
            valid.append(guess)
            score += points[len(guess)]
            display()
            print(f"Good job! {guess} is a valid word worth {points[len(guess)]} points.")


play()