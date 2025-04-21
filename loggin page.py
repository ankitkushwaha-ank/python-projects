import json
import os

FILE_NAME = "data.json"


# Function to load users from file
def load_users():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)  # Load JSON file into dictionary
        except json.JSONDecodeError:
            return {}  # Return empty dictionary if file is empty or corrupted
    return {}  # Return empty dictionary if file doesn't exist


# Function to save users to file
def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)  # Save dictionary as JSON


# Function to register a new user
def register():
    users = load_users()

    username = input("Enter a new username: ")

    if username in users:
        print("❌ Username already exists! Try again.")
        return

    password = input("Enter a new password: ")

    users[username] = password  # Save username and password pair
    save_users(users)

    print("✅ Registration successful!")


# Function to login user
def login():
    users = load_users()

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists and password matches
    if username in users and users[username] == password:
        print("✅ Login Successful!")
    else:
        print("❌ Invalid Username or Password! Please try again.")


# Main program loop
while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("🔴 Exiting the program. Goodbye!")
        break
    else:
        print("❌ Invalid option! Please choose 1, 2, or 3.")
