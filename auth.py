# auth.py

import hashlib

# Path to the user data file
USER_DATA_FILE = "users.txt"

# Function to hash passwords for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user():
    print("\n--- Register ---")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    hashed_password = hash_password(password)
    
    # Check if username already exists
    with open(USER_DATA_FILE, "a+") as f:
        f.seek(0)
        for line in f:
            stored_username, _ = line.strip().split(":")
            if stored_username == username:
                print("Username already exists. Try logging in.")
                return False
    
    # Save new user's credentials
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username}:{hashed_password}\n")
    print("Registration successful!")
    return True

# Function to log in an existing user
def login_user():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)
    
    # Verify user credentials
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            stored_username, stored_password = line.strip().split(":")
            if stored_username == username and stored_password == hashed_password:
                print("Login successful!")
                return True
    print("Incorrect username or password. Please try again.")
    return False
