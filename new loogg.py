import sqlite3 as sql

from adt import username

conn = sql.connect('user_info1.db')
cursor = conn.cursor()

#for create a database if not exist
# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    email_id TEXT UNIQUE)''')
conn.commit()

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    emial = input("enter you email: ")


    try:
        cursor.execute("INSERT INTO users (username, password,email_id) VALUES (?, ?, ?)", (username, password, emial))
        conn.commit()
        print("✅ Registration successful!")
    except sql.IntegrityError:
        print("❌ Username already exists! Try again.")



#for login the user
def login():
    username = input('enter your user name: ')
    password = input('enter your password: ')

    cursor.execute('SELECT * FROM users WHERE username = ? AND password =?' ,(username,password))
    user = cursor.fetchone()

    if user:
        print('login successfully')
    else:
        print('invalid credentials')


register()
conn.close()