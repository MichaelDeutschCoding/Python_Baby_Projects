from random import choices

colors = ["r", "o", "w", "b", "g", "y"]
color_dict = {"r": "red", "o": "orange", "w": "white", "b": "black", "g": "green", "y": "yellow"}


def make_code():
    return choices(colors, k=4)

def grade(guess, code):
    reds = 0
    whites = 0

    for color in colors:
        whites += min(code.count(color), guess.count(color) )

    for i in range(4):
        if guess[i] == code[i]:
            reds += 1
            whites -= 1
    
    print(f"\nYou guessed: {color_dict[guess[0]]:^5} {color_dict[guess[1]]:^5} {color_dict[guess[2]]:^5} {color_dict[guess[3]]:^5}  | It scored {reds} reds and {whites} whites.")
    return (guess, reds, whites)

def display(guesses):
    print()
    print('-'*70)
    for num, row in enumerate(guesses, 1):
	      print(f"| Guess #{num}: {color_dict[row[0][0]]:^8}{color_dict[row[0][1]]:^8}{color_dict[row[0][2]]:^8}{color_dict[row[0][3]]:^8} | Reds: {row[1]} | Whites: {row[2]} |")
    print('-'*70)


def play():
    print("Hello, and welcome to Mastermind. I'm now choosing a code.")
    print("Ok, I've chosen a code. You will try to guess it. The six possible colors are: black, white, red, orange, yellow, and green.")
    print("You may type 'q' at any time to quit.")
    code = make_code()
    #print(code)
    guesses = []

    while len(guesses) < 10:
        guess = input("Enter a four color guess using the first letter of each color: ").lower()

        if guess == 'q':
            print("Goodbye.")
            break
        
        if not len(guess) == 4:
            print("Sorry, please enter exactly four letters.")
            continue
        if not all([x in color_dict for x in guess]):
            print("You may only use the six available colors: black, white, red, orange, yellow, and green.")
            continue

        answer = grade(guess, code)
        guesses. append((answer))
        if answer[1] == 4:
            print(f"Congratulations! You won in {len(guesses)} turns!")
            break
        if (answer[1] + answer[2]) == 3:
            print("You're getting close!")
        if (answer[1] + answer[2]) == 4:
            print("You've got all the right colors. Just gotta figure out the correct order now.")
        if (answer[1] + answer[2]) == 0:
            print("Well, at least now you know what it's not!")
        
        display(guesses)
    else:
        print(f"Sorry, you're out of turns. The code was: {color_dict[code[0]]:^7} {color_dict[code[1]]:^7} {color_dict[code[2]]:^7} {color_dict[code[3]]:^7}")

def main():
    again = 'y'
    while again == 'y':
        play()
        again = input("Do you want to play again? Type 'Y' for yes. ").lower()

    print("Thanks for playing. Goodbye.")

main()