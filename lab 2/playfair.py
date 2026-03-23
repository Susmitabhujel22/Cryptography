import numpy as np

# Generate 5x5 Playfair matrix
def generateMatrix(key):
    key = key.replace("J", "I")
    matrix = []
    used = set()
    
    for char in key:
        if char not in used:
            matrix.append(char)
            used.add(char)
    
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # I/J combined
        if c not in used:
            matrix.append(c)
            used.add(c)
    
    return np.array(matrix).reshape(5,5)

# Find row, col of a letter
def findIndex(matrix, letter):
    pos = np.where(matrix == letter)
    return pos[0][0], pos[1][0]

# Prepare message: remove J, split repeated letters with X
def prepareMessage(message):
    message = message.replace("J", "I")
    message = list(message)
    i = 0
    while i < len(message):
        if i+1 == len(message):
            message.append("X")
        elif message[i] == message[i+1]:
            message.insert(i+1, "X")
        i += 2
    return message

# Encrypt message
def encryptMessage(message, key):
    matrix = generateMatrix(key)
    message = prepareMessage(message)
    cipher = ""
    
    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]
        r1,c1 = findIndex(matrix, a)
        r2,c2 = findIndex(matrix, b)
        
        if r1 == r2:  # same row
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # same column
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  # rectangle
            cipher += matrix[r1][c2] + matrix[r2][c1]
    
    return cipher

# Decrypt message
def decryptMessage(message, key):
    matrix = generateMatrix(key)
    message = list(message)
    plain = ""
    
    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]
        r1,c1 = findIndex(matrix, a)
        r2,c2 = findIndex(matrix, b)
        
        if r1 == r2:  # same row
            plain += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:  # same column
            plain += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:  # rectangle
            plain += matrix[r1][c2] + matrix[r2][c1]
    
    return plain

# Menu-driven program
choice = input("Enter 1 for Encryption or 2 for Decryption: ")

message = input("Enter your message: ").upper().replace(" ", "")
key = input("Enter the key: ").upper().replace(" ", "")

if choice == "1":
    cipher = encryptMessage(message, key)
    print("Encrypted Message:", cipher)
elif choice == "2":
    plain = decryptMessage(message, key)
    print("Decrypted Message:", plain)
else:
    print("Invalid choice!")

