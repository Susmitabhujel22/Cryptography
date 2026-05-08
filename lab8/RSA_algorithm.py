import math

# Function to find modular inverse using Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)

    gcd, x, y = egcd(e, phi)
    return x % phi

def rsa():
    # Step 1: Choose primes
    p = 17
    q = 19

    n = p * q
    phi = (p - 1) * (q - 1)

    # Step 2: Choose e
    e = 7
    while math.gcd(e, phi) != 1:
        e += 1

    # Step 3: Compute d
    d = mod_inverse(e, phi)

    print("Public Key (e, n):", (e, n))
    print("Private Key (d, n):", (d, n))

    # Step 4: Message input (text)
    message = input("Enter message: ")

    # Convert to ASCII values
    msg_nums = [ord(char) for char in message]

    # Encryption
    encrypted = [pow(m, e, n) for m in msg_nums]
    print("Encrypted:", encrypted)

    # Decryption
    decrypted = [chr(pow(c, d, n)) for c in encrypted]
    print("Decrypted:", ''.join(decrypted))


rsa()