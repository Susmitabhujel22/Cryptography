def encryptMessage(message, key):
    cipherText = ''
    r, c = 0, 0
    down = True
    matrix = [[None for _ in range(len(message))] for _ in range(key)]
    
    # Fill the zig-zag pattern
    for i in range(len(message)):
        matrix[r][c] = message[i]
        if down:
            r += 1
        else:
            r -= 1
        if r == key - 1:
            down = False
        elif r == 0:
            down = True
        c += 1
    
    # Read row by row to get ciphertext
    for row in matrix:
        for item in row:
            if item is not None:
                cipherText += item
    return cipherText

def decryptMessage(cipherText, key):
    # Create empty matrix
    matrix = [['\n' for _ in range(len(cipherText))] for _ in range(key)]
    
    # Mark positions with '*'
    r, c = 0, 0
    down = True
    for i in range(len(cipherText)):
        matrix[r][c] = '*'
        if down:
            r += 1
        else:
            r -= 1
        if r == key - 1:
            down = False
        elif r == 0:
            down = True
        c += 1
    
    # Fill the letters row by row
    index = 0
    for i in range(key):
        for j in range(len(cipherText)):
            if matrix[i][j] == '*' and index < len(cipherText):
                matrix[i][j] = cipherText[index]
                index += 1
    
    # Read the zig-zag to get original message
    result = ''
    r, c = 0, 0
    down = True
    for i in range(len(cipherText)):
        result += matrix[r][c]
        if down:
            r += 1
        else:
            r -= 1
        if r == key - 1:
            down = False
        elif r == 0:
            down = True
        c += 1
    
    return result

# Menu-driven program
choice = input("Enter 1 for Encryption or 2 for Decryption: ")
message = input("Enter your message: ").replace(" ", "")
key = int(input("Enter the number of rails: "))

if choice == "1":
    cipher = encryptMessage(message, key)
    print("Encrypted Message:", cipher)
elif choice == "2":
    plain = decryptMessage(message, key)
    print("Decrypted Message:", plain)
else:
    print("Invalid choice!")