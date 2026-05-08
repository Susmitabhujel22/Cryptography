import random

def diffie_hellman():
    # Public values
    p = 29   # prime number
    g = 2   # primitive root

    print("Public values:")
    print("p =", p, ", g =", g)

    # Private keys (chosen by users)
    a = int(input("Enter private key of User A: "))
    b = int(input("Enter private key of User B: "))

    # Public keys
    A = pow(g, a, p)
    B = pow(g, b, p)

    print("Public key of A:", A)
    print("Public key of B:", B)

    # Shared secret key
    key_A = pow(B, a, p)
    key_B = pow(A, b, p)

    print("Shared key (A):", key_A)
    print("Shared key (B):", key_B)

    # Encryption using shared key (XOR method)
    message = input("Enter message: ")

    encrypted = [ord(ch) ^ key_A for ch in message]
    print("Encrypted message:", encrypted)

    # Decryption
    decrypted = ''.join(chr(ch ^ key_B) for ch in encrypted)
    print("Decrypted message:", decrypted)


diffie_hellman()