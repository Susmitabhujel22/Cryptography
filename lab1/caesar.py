import string

def encryption(plainText, key):

    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase

    cipherText = ''

    for letter in plainText:

        if letter in lowerCase:
            index = lowerCase.index(letter)
            shiftedindex = (index + key) % 26
            cipherText += lowerCase[shiftedindex]

        elif letter in upperCase:
            index = upperCase.index(letter)
            shiftedindex = (index + key) % 26
            cipherText += upperCase[shiftedindex]

        else:
            cipherText += letter

    return cipherText


def decryption(cipherText, key):

    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase

    plainText = ''

    for letter in cipherText:

        if letter in lowerCase:
            index = lowerCase.index(letter)
            shiftedindex = (index - key) % 26
            plainText += lowerCase[shiftedindex]

        elif letter in upperCase:
            index = upperCase.index(letter)
            shiftedindex = (index - key) % 26
            plainText += upperCase[shiftedindex]

        else:
            plainText += letter

    return plainText


message = "Susmitalab"
key = 4

encrypted = encryption(message, key)
decrypted = decryption(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)