from random import randrange, choices

class Account:

    def __init__(self, name, balance = 0, account_type = 'savings', fname = None):
        self.name = name
        self.at = account_type
        self.balance = balance
        self.fname = fname

    def __str__(self):
        return f"This {self.at} account belongs to {self.name}. \
Current balance is: ${self.balance:,.2f}."

    def __repr__(self):
        return f"Name (nickname): {self.name:<20}({self.fname:^8}) | Account type: {self.at:<10} | Balance: {self.balance:,.2f}"

    def greet(self):
        if self.fname:
            print(f"Hello {self.fname}, welcome back!")
        else:
            print(f"Hello {self.name}, welcome to your bank account.")
        print("\tWhat would you like to do today?")
        option = '!'
        while option not in 'DWTB':
            option = input("Type 'D' for deposit, 'W' to withdraw, 'T' for transfer, \
or 'B' for your balance. ").upper()

            if option == 'Q':
                return

            if option == 'D':
                print("\nOk, a deposit.")
                self.deposit()
                again = input("Can I help you with anything else? ").upper()
                if again.startswith('Y'):
                    option = '!'
                    continue

            elif option == 'W':
                print(f"\nGreat, let's make a withdrawal. Your current balance is ${self.balance:,.2f}.")
                self.withdraw()
                again = input("Would you like help with anything else? ").upper()
                if again.startswith('Y'):
                    option = '!'
                    continue

            elif option == 'T':
                self.transfer()
                again = input("Anything else? ").upper()
                if again.startswith('Y'):
                    option = '!'
                    continue

            elif option == 'B':
                print('\n' + str(self))
                again = input("Would you like to do anything else? ").upper()
                if again.startswith('Y'):
                    option = '!'
                    continue        

    def deposit(self):
        while True:
            dep_num = input("\tHow much would you like to deposit? ")
            try:
                dep_num = float(dep_num)
                assert(dep_num > 0)
                break
            except ValueError:
                print("Sorry. That's not a valid entry.")
                continue
            except AssertionError:
                print("You can't deposit nothing!")
                continue
        print(f"Depositing ${dep_num:.2f} into {self.name}'s {self.at} account.")
        self.balance += dep_num
        print(f"Current balance is now: ${self.balance:,.2f}")
        print("Thank you.")        

    def withdraw(self):
        while True:
            withdraw_num = input("\tHow much would you like to withdraw? ")
            try:
                withdraw_num = float(withdraw_num)
                if withdraw_num < 0:
                    print("Must be positive number.")
                    continue
                assert(withdraw_num <= self.balance)
                break
            except ValueError:
                print("Sorry. That's not a valid entry.")
                continue
            except AssertionError:
                print(f"Insufficient funds. Your current balance is ${self.balance:.2f}.")
                continue

        print(f"Withdrawing ${withdraw_num:.2f} from {self.name}'s {self.at} account.")
        self.balance -= withdraw_num
        print(f"Current balance is now: ${self.balance:,.2f}")
        print("Thank you.")

    def transfer(self):

        while True:
            rec = input("What account number do you want to send it to? ").upper()
            if rec == 'Q':
                return
            if rec in master.keys():
                break
            else:
                print("Account not found. Try again.")
                continue
            
        while True:
            amount = input(f"How much do you want to send? Your current balance is ${self.balance:,.2f}? ")
            try:
                amount = float(amount)
                assert(self.balance >= amount)
                if amount < 0:
                    print("Must be positive number.")
                    continue
                self.balance -= amount
                master[rec].balance += amount
                break
            except ValueError:
                print("Sorry, invalid number.")
                continue
            except AssertionError:
                print("Insufficient funds.")
                continue

        print(f"Transfering ${amount} from {self.name}'s account to {master[rec].name}.")
        print(f"Your remaining balance is ${self.balance:,.2f}")


master = {}

def new_account():
    print("Welcome. Let's get you on your way opening your new account.")

    raw_name = input("Enter your full name. \
If you have a nickname you'd like to be called, type it after a semicolon. ")
    if ';' in raw_name:
        name, fname = raw_name.split(';')
        name, fname = name.strip(), fname.strip()
    else:
        name, fname = raw_name, raw_name.split()[0]

    at = input("What type of account would you like to open? ")
    if at:
        at = at
    else:
        at = 'savings'

    while True:
        balance = input("Our minimum starting balance is $200. How much would you like to deposit? ")
        if balance == 'Q':
            print("Sorry to see you go. Goodbye.")
            return
        try:
            balance = float(balance)
            assert(balance >= 200)
            break
        except ValueError:
            print("I'm sorry, that's not a valid entry.")
            continue
        except AssertionError:
            print("Sorry that's below our minimum balance.")
            continue
    code = random_code()
    master[code] = Account(name, balance, at, fname = fname)

    print(f"Ok {fname}, you're good to go! You've successfully opened a {at} account \
with an opening balance of ${balance:,.2f}.")
    print(f"Your account number is: {code}. Please save this for future reference.")
    return  
            
def random_code():
    letters = ''.join(choices('ABCDEF', k = 1))
    numbers = str(randrange(100, 1000))
    code = ''.join([letters, numbers])
    return code
    
def access():
    print("hello")
    attempts_remaining = 3
    while attempts_remaining > 0:
        code = input("What's your account code? ").upper()
        if code == 'ADMIN':
            print('\t ADMIN MASTER ACCOUNT LIST\n'
                  '\t===========================')
            for key, value in master.items():
                print(f"Acc num: {key:>5} | {value!r}")
            break
                
        elif code in master.keys():
            print("you're in.")
            master[code].greet()
            break

        elif code == 'NEW':
            new_account()
            break
            
        else:
            attempts_remaining -= 1
            print(f"Sorry, that's not a correct account code. You are allowed {attempts_remaining} more attempts.")
    else:
        print("You've exceeded maximum number of failed attempts. Goodbye.")
            
            
master['MIKE'] = Account('Michael Deutsch', 500, 'checking', 'Mike')
master['BT'] = Account('Beatrice Rose', 100000, 'investment', 'Beatie')
master['LM330'] = Account('Leah Miriam', 300, fname = 'Lucy')
master['geula'] = Account("Geula Deutsch", account_type = 'family')
bz = Account("Bentzion Deutsch")

master['A123'] = Account('George Washington', 1000, 'savings', 'GeeDub')


