from random import choices, shuffle

with open("D:\\sgb-words.txt") as f:
    words = f.read().splitlines()

vowels = list('aeiou')
cons = list('bcdfghjklmnpqrstvwxyz')
vw =  [4,4,4,3,2]
cw = [5,6,6,5,5,7,4,4,7,7,6,5,2,7,8,8,3,4,2,4,2]

"""
print('vowels:', list(zip(vowels, vw)))
print('consonants:', list(zip(cons, cw)))
"""
def test(word, letters):
    pool = list(letters)
    for letter in word:
        try:
            pool.remove(letter)
        except ValueError:
            return False
    return True

def answers(v = 3, c = 6):
    valid = []
    letters = choices(vowels, weights = vw, k = v) + choices(cons, weights = cw, k = c)
    print(letters)
    for word in words:
        if test(word, letters):
            valid.append(word)
    #print(f"vowels: {v}; consonants: {c}. Words: {len(valid)}")
    return valid


def main():
    print("Hello and welcome to word anagrams.")
    v = input("You get nine letters. How many of those would you like to be vowels? ")
    try:
        v = int(v)
    except ValueError:
        v =4
    if not 1 <= v <= 8:
        v = 4
    c = 9 - v
    letters = choices(vowels, weights = vw, k = v) + choices(cons, weights = cw, k = c)
    shuffle(letters)
    valid = []
    for word in words:
        if test(word, letters):
            valid.append(word)
    print(f'Your letters are: {" ".join([l.upper() for l in letters])}. I\'ve found {len(valid)} five-letter words with your letters.')

    guessed = []
    while True:
        guess = input("Type a five-letter word that can be made with your letters: (type 'show!' to see the letters again)").lower()

        if guess == 'cheat!':
            print("Ok, you cheater! Here you go...\n")
            print(valid)
            continue
        elif guess == 'quit!':
            print('Sorry to see you go. Goodbye.')
            break
        elif guess == 'show!':
            print(' '.join((l.upper() for l in letters)))
            continue
        elif len(guess) != 5:
            print("We can only accept five letter words.")
            continue
        elif guess in guessed:
            print("You've already guessed that word.")
            continue
        elif guess in valid:
            guessed.append(guess)
            if len(guessed) == len(valid):
                print(f"{guess.upper()} is a valid word. Congratulations! You won!")
                again = input("Do you want to play again? ").upper()
                if again.startswith('Y'):
                    main()
                break
            print(f"Good. {guess.upper()} is a valid word. {len(guessed)} so far, {len(valid) - len(guessed)} to go.")
            continue
        for let in set(guess):
            if guess.count(let) > letters.count(let):
                if letters.count(let) == 0:
                    print(f"The letter '{let}' is not available.", end = ' ')
                else:
                    print(f"You only have {letters.count(let)} '{let}'s available. {guess} requires {guess.count(let)}.", end = ' ')

        else:
            print('Not a valid word.')

main()5