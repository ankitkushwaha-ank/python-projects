import sqlite3

# Connect to SQLite database (creates 'users.db' if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT)''')
conn.commit()


# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registration successful!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists! Try again.")

# Function to login user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
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

# Close the database connection when done
conn.close()
