import random

# Function to compute modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise Exception("Inverse does not exist")
    return x % m

# ElGamal Encryption and Decryption
def elgamal():
    # Step 1: Public parameters (prime p and generator g)
    p = int(input("Enter a prime number p: "))
    g = int(input(f"Enter a primitive root g of {p}: "))

    # Step 2: Private key (x) and Public key (y)
    x = random.randint(1, p-2)   # private key
    y = pow(g, x, p)              # public key
    print(f"\nPublic key (p, g, y): ({p}, {g}, {y})")
    print(f"Private key x: {x}")

    # Step 3: Message input
    message = input("\nEnter message to encrypt: ")
    msg_nums = [ord(char) for char in message]  # convert to numbers

    # Step 4: Encryption
    k = random.randint(1, p-2)   # ephemeral key
    c1 = pow(g, k, p)             # first part of cipher
    c2_list = [(m * pow(y, k, p)) % p for m in msg_nums]  # second part
    print("\nEncrypted message:")
    print("c1 =", c1)
    print("c2 =", c2_list)

    # Step 5: Decryption
    decrypted_nums = [(c2 * mod_inverse(pow(c1, x, p), p)) % p for c2 in c2_list]
    decrypted_message = ''.join([chr(num) for num in decrypted_nums])
    print("\nDecrypted message:", decrypted_message)

# Run the ElGamal program
elgamal()