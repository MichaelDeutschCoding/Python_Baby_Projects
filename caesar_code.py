"""
Program to encrypt and decrypt a 'Caesar Code' for a given string.
"""


def main():
    s = input("\nEnter the string you'd like to encrypt: ")
    while True:
        n = input("How many characters would you like to shift? (Enter a number): ")
        try:
            n = int(n)
            break
        except ValueError:
            print("Must be a number.")
    print(cipher(s, n))
    

def shift_car(c, n):
    if c.islower():
        return chr(((ord(c) - 97 + n) % 26) + 97)
    elif c.isupper():
        return chr(((ord(c)- 65 + n) % 26) + 65)
    else:
        return c

def cipher(s, n):
    result = ''
    for c in s:
        result += shift_car(c, n)
    return result


print('\noutcome of cipher (n = 5): Hello World')
print(cipher('Hello World', 5))

print('\noutcome of Cipher (n = -5): Hello World')
print(cipher('Hello World', -5))

print('\noutcome of cipher (n = -5): Mjqqt btwqi')
print(cipher('Mjqqt btwqi', -5))

print()
print(cipher("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj", 2))

main()