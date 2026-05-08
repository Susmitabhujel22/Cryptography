import hashlib

# Step 1: Input message
message = input("Enter the message to hash: ")
print("Original Message:", message)

# Step 2: Convert message to bytes
message_bytes = message.encode()
print("Message in Bytes:", message_bytes)

# Step 3: Create MD5 hash object
md5_hash = hashlib.md5()

# Step 4: Feed the message bytes into the hash object
md5_hash.update(message_bytes)

# Step 5: Generate the hexadecimal digest (hash value)
hash_value = md5_hash.hexdigest()
print("MD5 Hash Value:", hash_value)