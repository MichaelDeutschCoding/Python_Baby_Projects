class AgeConverter:
    "Converts input age of years into other measurements."

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if type(self.age) != int:
            raise ValueError("You must enter age as a number.")
        elif self.age < 0 or self.age > 110:
            raise ValueError("Are you sure you got your age right?")


    def convert_to_months(self):
        self.months = self.age * 12
        return self.months

    def convert_to_days(self):
        self.days = self.age * 365
        return self.days

    def convert_to_hours(self):
        self.hours = self.age * 365 * 24
        return self.hours

    def convert_to_seconds(self):
        self.seconds = self.age * 365 * 24 *3600
        return self.seconds

def main():
    print("Hello, and thank you for using the Age Converter.")
    user = input("Please enter your name: ").capitalize()
    age = input("And how old are you, %s? " % user)
    try:
        age = int(age)
    except ValueError:
        print("You must enter your age as nnnnummmmber")
    user = AgeConverter(user, age)
    while True:
        conversion = input("What measurement would you like to convert your age to?  \
Type 'M' for months, 'D' for days, 'H' for hours, and 'S' for seconds. ").upper()
        if conversion == 'M':
            user.convert_to_months()
            print("%s is %s years old, which is approximately %s months." \
                  % (user.name, user.age, user.months))
            break
        if conversion == 'D':
            user.convert_to_days()
            print("%s is %s years old, which is approximately %s days." \
                  % (user.name, user.age, user.days))
            break
        if conversion == 'H':
            user.convert_to_hours()
            print("%s is %s years old, which is approximately %s hours." \
                  % (user.name, user.age, "{:,}".format(user.hours)))
            break
        if conversion == "S":
            user.convert_to_seconds()
            print("%s is %s years old, which is approximately %s seconds." \
                  % (user.name, user.age, "{:,}".format(user.seconds)))
            break
        else:
            print("Invlid entry.")
            continue


main()    
blah = input("MD")   
    
    
        
