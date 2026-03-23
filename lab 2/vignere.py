import string

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase

def encryptMessage(plainText, key):
    cipherText = ""
    key = key.lower()
    keylen = len(key)
    count = 0

    for letter in plainText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shifter = lowerCase.index(key[count % keylen])
            cipherText += lowerCase[(index + shifter) % 26]
            count += 1

        elif letter in upperCase:
            index = upperCase.index(letter)
            shifter = lowerCase.index(key[count % keylen])
            cipherText += upperCase[(index + shifter) % 26]
            count += 1

        else:
            cipherText += letter

    return cipherText


def decryptMessage(cipherText, key):
    plainText = ""
    key = key.lower()
    keylen = len(key)
    count = 0

    for letter in cipherText:
        if letter in lowerCase:
            index = lowerCase.index(letter)
            shifter = lowerCase.index(key[count % keylen])
            plainText += lowerCase[(index - shifter) % 26]
            count += 1

        elif letter in upperCase:
            index = upperCase.index(letter)
            shifter = lowerCase.index(key[count % keylen])
            plainText += upperCase[(index - shifter) % 26]
            count += 1

        else:
            plainText += letter

    return plainText

message = input("Enter your message: ")

print("\nChoose an option:")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter 1 or 2: ")
key = input("Enter the secret key: ")

if choice == "1":
    result = encryptMessage(message, key)
    print("\nEncrypted Message:", result)

elif choice == "2":
    result = decryptMessage(message, key)
    print("\nDecrypted Message:", result)

else:
    print("\nInvalid choice! Please select 1 or 2.")
