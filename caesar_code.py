"""Program to encrypt and decrypt a 'Caesar Code' for a given string."""



"""
def encrypt():

    s = input("Enter the sentence you wish to encrypt: ").lower()
    while True:
        n = input('How many letters would you like to shift? (-20 through 20) ')
        try:
            n = int(n)
            assert(-20 < n < 20)
            break
        except ValueError:
            print("Must be a number.")
        except AssertionError:
            print("Number out of range.")

"""

    

def shift_car(c, n):
    if c.islower():
        return chr(((ord(c) - 97 + n) % 26) + 97)
    elif c.isupper():
        return chr(((ord(c)- 65 + n) % 26) + 65)
    else:
        return c

def cipher(s, n):
    m = ''
    for c in s:
        m += shift_car(c, n)
    return m


print('\noutcome of cipher (n = 5): Hello World')
print(cipher('Hello World', 5))


print('\noutcome of Cipher (n = -5): Hello World')
print(cipher('Hello World', -5))


print('\noutcome of cipher (n = -5): Mjqqt btwqi')
print(cipher('Mjqqt btwqi', -5))


print(cipher("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj", 2))