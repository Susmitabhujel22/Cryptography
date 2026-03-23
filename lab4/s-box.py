# ------------------ S-DES IMPLEMENTATION ------------------

# Permutation function
def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

# Left circular shift
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# XOR function
def xor(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a, b))

# S-Boxes
S0 = [
    [1,0,3,2],
    [3,2,1,0],
    [0,2,1,3],
    [3,1,3,2]
]

S1 = [
    [0,1,2,3],
    [2,0,1,3],
    [3,0,1,0],
    [2,1,0,3]
]

# Key generation
def generate_keys(key):
    P10 = [3,5,2,7,4,10,1,9,8,6]
    P8  = [6,3,7,4,8,5,10,9]

    key = permute(key, P10)
    left, right = key[:5], key[5:]

    # K1
    left1 = left_shift(left,1)
    right1 = left_shift(right,1)
    K1 = permute(left1 + right1, P8)

    # K2
    left2 = left_shift(left1,2)
    right2 = left_shift(right1,2)
    K2 = permute(left2 + right2, P8)

    return K1, K2

# Feistel function
def fk(bits, key):
    EP = [4,1,2,3,2,3,4,1]
    P4 = [2,4,3,1]

    left, right = bits[:4], bits[4:]

    right_expanded = permute(right, EP)
    xor_result = xor(right_expanded, key)

    left_part = xor_result[:4]
    right_part = xor_result[4:]

    # S0
    row = int(left_part[0] + left_part[3], 2)
    col = int(left_part[1] + left_part[2], 2)
    s0_val = format(S0[row][col], '02b')

    # S1
    row = int(right_part[0] + right_part[3], 2)
    col = int(right_part[1] + right_part[2], 2)
    s1_val = format(S1[row][col], '02b')

    sbox_output = permute(s0_val + s1_val, P4)

    left_result = xor(left, sbox_output)

    return left_result + right

# Encrypt block
def encrypt_block(block, K1, K2):
    IP = [2,6,3,1,4,8,5,7]
    IP_INV = [4,1,3,5,7,2,8,6]

    block = permute(block, IP)

    temp = fk(block, K1)
    temp = temp[4:] + temp[:4]  # swap

    temp = fk(temp, K2)

    return permute(temp, IP_INV)

# Decrypt block
def decrypt_block(block, K1, K2):
    IP = [2,6,3,1,4,8,5,7]
    IP_INV = [4,1,3,5,7,2,8,6]

    block = permute(block, IP)

    temp = fk(block, K2)
    temp = temp[4:] + temp[:4]  # swap

    temp = fk(temp, K1)

    return permute(temp, IP_INV)

# Convert string to binary
def string_to_binary(text):
    return ''.join(format(ord(c), '08b') for c in text)

# Convert binary to string
def binary_to_string(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

# Encrypt full message
def encrypt_message(message, key):
    K1, K2 = generate_keys(key)
    binary = string_to_binary(message)
    encrypted = ""
    for i in range(0, len(binary), 8):
        encrypted += encrypt_block(binary[i:i+8], K1, K2)
    return encrypted

# Decrypt full message
def decrypt_message(cipher, key):
    K1, K2 = generate_keys(key)
    decrypted_binary = ""
    for i in range(0, len(cipher), 8):
        decrypted_binary += decrypt_block(cipher[i:i+8], K1, K2)
    return binary_to_string(decrypted_binary)

# ------------------ MAIN ------------------

message = "Aqua Berg"
key = "1100110100"

print("Original Message:", message)

cipher = encrypt_message(message, key)
print("Encrypted (Binary):", cipher)

decrypted = decrypt_message(cipher, key)
print("Decrypted Message:", decrypted)