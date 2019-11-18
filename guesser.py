print("\nHello, and welcome to the Number Guesser.\nPlease guess a number between 1-100.\nOn each guess, type 'yes', 'too high', or 'too low'.")

a = 42
counter = 1
won = False
low, high = 1, 101
while not won:
    middle = (low + high)// 2
    if low == high:
        print("Uh oh! Looks like somebody made a mistake.")
        break
    response = input('Is your number %d? ' % middle)
    if response == 'yes':
        won = True
        print("I won in %d guesses!" % counter)
        break
    elif response == 'too high':
        high = middle
        counter +=1
        continue
    elif response == 'too low':
        low = middle
        counter +=1
        continue
    else:
        print("I'm sorry, that's an invalid response. Please type either 'yes', 'too high', or 'too low'.")
        continue

