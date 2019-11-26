from random import randint
number = randint(1,10)

def play():
    guess = int(input("Let's play a game!\nI'm thinking of a number between 1-10. What's your guess? "))
    while True:
        if guess == number:
            print("Congrats, you win!")
            break
        elif guess > number:
            guess = int(input("Too high. Guess again: "))
        elif guess < number:
            guess = int(input("Too low. Guess again: "))
        else:
            break

play()

while True:
    c = input("Game over. Do you want to play again? Type Y for yes. ")
    if "Y" not in c:
        break
    else:
        play()


