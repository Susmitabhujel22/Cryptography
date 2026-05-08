import hashlib

# Step 1: Input message
message = input("Enter the message to hash: ")
print("Original Message:", message)

# Step 2: Convert message to bytes
message_bytes = message.encode()
print("Message in Bytes:", message_bytes)

# Step 3: Create SHA-256 hash object
sha256_hash = hashlib.sha256()

# Step 4: Feed the message bytes into the hash object
sha256_hash.update(message_bytes)

# Step 5: Generate the hexadecimal digest (hash value)
hash_value = sha256_hash.hexdigest()
print("SHA-256 Hash Value:", hash_value)