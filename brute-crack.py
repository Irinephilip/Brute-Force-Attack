import hashlib

# Step 1: Read the hashes file
with open("hashes.txt", "r") as f:
    lines = f.readlines()

# Step 2: Parse each line into username and hash
user_hashes = []
for line in lines:
    line = line.strip()  # Remove newline character
    username, hash_value = line.split(":")
    user_hashes.append((username, hash_value))

# Step 3: Read passwords from the wordlist
with open("wordlist.txt", "r") as f:
    passwords = [line.strip() for line in f.readlines()]

# Step 4: Try each password for each user
for username, hash_value in user_hashes:
    found = False
    for password in passwords:
        hashed = hashlib.md5(password.encode()).hexdigest()
        if hashed == hash_value:
            print(f"{username}'s password is: {password}")
            found = True
            break
    if not found:
        print(f"Could not crack password for {username}")
