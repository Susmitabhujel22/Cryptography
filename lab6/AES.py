from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Take message from user
message = input("Enter your message: ")

# Predefined key (16 bytes)
key = b'abcdef1234567890'

# Generate IV
iv = get_random_bytes(16)

# Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))

print("\n--- Encryption ---")
print("Original Message:", message)
print("Cipher Text:", ciphertext)

# Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("\n--- Decryption ---")
print("Decrypted Message:", decrypted.decode())