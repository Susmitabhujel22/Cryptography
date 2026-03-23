import numpy as np
from math import gcd

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)

def mod_inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_mod_inverse_3x3(matrix, modulus):
    det = int(round(np.linalg.det(matrix))) % modulus
    if gcd(det, modulus) != 1:
        raise ValueError("Key matrix is not invertible modulo 26")
    det_inv = mod_inverse(det, modulus)

    adj = np.zeros((3,3), dtype=int)
    adj[0,0] = matrix[1,1]*matrix[2,2] - matrix[1,2]*matrix[2,1]
    adj[0,1] = -(matrix[0,1]*matrix[2,2] - matrix[0,2]*matrix[2,1])
    adj[0,2] = matrix[0,1]*matrix[1,2] - matrix[0,2]*matrix[1,1]

    adj[1,0] = -(matrix[1,0]*matrix[2,2] - matrix[1,2]*matrix[2,0])
    adj[1,1] = matrix[0,0]*matrix[2,2] - matrix[0,2]*matrix[2,0]
    adj[1,2] = -(matrix[0,0]*matrix[1,2] - matrix[0,2]*matrix[1,0])

    adj[2,0] = matrix[1,0]*matrix[2,1] - matrix[1,1]*matrix[2,0]
    adj[2,1] = -(matrix[0,0]*matrix[2,1] - matrix[0,1]*matrix[2,0])
    adj[2,2] = matrix[0,0]*matrix[1,1] - matrix[0,1]*matrix[1,0]

    inv_matrix = (det_inv * adj) % modulus
    return inv_matrix

def hill_encrypt(plaintext, key):
    n = key.shape[0]
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % n != 0:
        plaintext += 'X'
    ciphertext = ""
    for i in range(0, len(plaintext), n):
        block = plaintext[i:i+n]
        block_vector = np.array(text_to_numbers(block)).reshape(n, 1)
        cipher_vector = np.dot(key, block_vector) % 26
        ciphertext += numbers_to_text(cipher_vector.flatten())
    return ciphertext

def hill_decrypt(ciphertext, key):
    n = key.shape[0]
    key_inv = matrix_mod_inverse_3x3(key, 26)
    plaintext = ""
    for i in range(0, len(ciphertext), n):
        block = ciphertext[i:i+n]
        block_vector = np.array(text_to_numbers(block)).reshape(n, 1)
        plain_vector = np.dot(key_inv, block_vector) % 26
        plaintext += numbers_to_text(plain_vector.flatten())
    return plaintext

key_matrix = np.array([[6,24,1],[13,16,10],[20,17,15]])
plaintext = "cryptolab"

ciphertext = hill_encrypt(plaintext, key_matrix)
decrypted = hill_decrypt(ciphertext, key_matrix)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
