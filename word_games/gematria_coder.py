#wordlist = ['אבגד', 'אאבג', 'אגבשק', 'איבד', 'יבדג']


wordlist = []

with open("Hebrew_wordlist.txt", "r", encoding="utf-8") as f:
    for line in f:
        wordlist.append(line.rstrip())

simplified_gematria = {
    'א' : '1',
    'ב' : '2',
    'ג' : '3',
    'ד' : '4',
    'ה' : '5',
    'ו' : '6',
    'ז' : '7',
    'ח' : '8',
    'ט' : '9',
    'י' : '1',
    'כ' : '2',
    'ל' : '3',
    'מ' : '4',
    'נ' : '5',
    'ס' : '6',
    'ע' : '7',
    'פ' : '8',
    'צ' : '9',
    'ק' : '1',
    'ר' : '2',
    'ש' : '3',
    'ת' : '4',
    'ך' : '2',
    'ם' : '4',
    'ן' : '5',
    'ף' : '8',
    'ץ' : '9'
}

def check_word(word, code):
    if len(word) != len(code):
        return False
    numbers = list(code)
    for letter in word:
        #print("length of 'numbers'", len(numbers))
        #print("checking", letter)
        try:
            numbers.remove(simplified_gematria[letter])
        except ValueError:
            return False
    assert(len(numbers) == 0)
    return True

def encoder(code):
    results = []
    for word in wordlist:
        if check_word(word, code):
            results.append(word)
    print(f"We've found {len(results)} words that match your code: {code}.\nHere they are")
    print("=" * 15)
    for item in results:
        print(item[::-1])
    print("=" * 15)

def validate(user_in):
    if not 4 <= len(user_in) <= 6:
        print("Code must be between 4-6 numbers.")
        return False
    if not all([d.isnumeric() for d in user_in]):
        print("May only use numbers.")
        return False
    if '0' in user_in:
        print("Sorry, there is no '0' in Gematria.")
        return False
    return True

def main():
    print("Hello. Welcome...")
    while True:
        while True:
            code = input("Enter your number code: ")
            if code == "Q":
                return
            if validate(code):
                break
        encoder(code)
        again = input("Would you like to do another code? (type 'y' for yes) ").lower()
        if again != "y":
            return

main()