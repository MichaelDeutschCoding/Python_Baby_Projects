from statistics import mean

#grades = {}
grades = {"Jeff": [95, 80, 77], 'Sally': [100, 93, 85], "Billy Bob": [66, 40, 33]}

def enter_grade():
    print("Entering a grade.")
    name = input("Student Name: ")
    try:
        grade = int(input("Grade: "))
    except ValueError:
        print("Invalid grade.")
        return
    if name in grades:
        grades[name].append(grade)
        print(grades[name])
    else:
        grades[name] = [grade]
        print(name, 'added to gradebook with one entry:', grade)
    
def remove_student():
    name = input("Which student would you like to remove? ")
    try:
        del grades[name]
        print("Successfully deleted", name)
    except KeyError:
        print("That's not a valid student name.")
        again = input("Would you like to try again? ")
        if 'y' in again or 'Y' in again:
            remove_student()

def grade_avg(name):
    
    av = mean(grades[name])
    if av >=90:
        let = 'A'
    elif av >= 80:
        let = 'B'
    elif av >= 70:
        let = 'C'
    elif av >= 60:
        let = 'D'
    else:
        let = 'F'
    return (av, let)

def options():
    while True:
        print("\n\tWelcome to Grade Central\n")
        print("\t[1] - Enter Grade")
        print("\t[2] - Remove Student")
        print("\t[3] - Student's Average Grades")
        print("\t[4] - Student List")
        print("\t[5] - All Students Averages")
        print("\t[6] - Exit\n")
        selection = input("What would you like to do? ")
        if selection == '1':
            enter_grade()
        elif selection == '2':
            remove_student()
        elif selection == '3':
            name = input("Which student's grades would you like to calculate? ")
            if not name in grades:
                print("Not a valid student name.")
            else:
                av, let = grade_avg(name)
                print(f"{name}'s grades: {grades[name]} \nGrade Average: {av:.2f} for a letter grade of: '{let}'.")

        elif selection == '4':
            print(list(grades))
        elif selection == '5':
            total = 0
            for student in grades:
                avg, let = grade_avg(student)
                total += avg
                print(f" Name: {student:<15}Grade average: {avg:.2f}  Letter grade: {let}")
            print(f"Class average: {total/len(grades):.2f}")
        elif selection == '6':
            print("Thank you for using Grade Central. Goodbye.")
            return
        else:
            print("Invalid selection.")


users = {'principal': 'pass123', 'smith': 'secret'}

def login():
    attempts = 0
    while attempts < 3:
        username = input("What's your username: ")
        if username not in users:
            attempts +=1
            print("Invalid username. Attempts:", attempts)
            continue
        password = input("Type your password: ")
        if not password == users[username]:
            attempts +=1
            print("Wrong password. Attempts:", attempts)
            continue
        else:
            options()
            return
    else:
        print("You've exceeded your number of attempts. Goodbye.")
    
#login()    
options()