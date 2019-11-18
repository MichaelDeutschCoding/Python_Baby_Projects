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
def encrypt(s, n):

    s = s.lower()
    
    uni = [ord(_) for _ in s]

    shifted = []
    for _ in uni:
        if _  < 97 or _ > 122:
            shifted.append(_)
        elif 97 <= _ + n <= 122:
            shifted.append(_ + n)
        elif n > 0:
            shifted.append(_ + n - 26)
        else:
            shifted.append(_ + n + 26) 

    letters = [chr(i) for i in shifted]

    return (''.join(letters).capitalize())
    

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



print('outcome of Encrypt (n = 5): Hello World')
print(encrypt('Hello World', 5))


print('\noutcome of cipher (n = 5): Hello World')
print(cipher('Hello World', 5))


print('\noutcome of Encrypt (n = -5): Hello World')
print(encrypt('Hello World', -5))

print('\noutcome of Cipher (n = -5): Hello World')
print(cipher('Hello World', -5))

print('\noutcome of encrypt (n = -5): Mjqqt btwqi')
print(encrypt('Mjqqt btwqi', -5))

print('\noutcome of cipher (n = -5): Mjqqt btwqi')
print(cipher('Mjqqt btwqi', -5))


print(cipher("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj", 2))