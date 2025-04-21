import sqlite3 as sql


conn = sql.connect('user_info.db')
cursor = conn.cursor()

#for create a database if not exist
# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    email_id TEXT UNIQUE)''')
conn.commit()
# c = cursor.execute('DROP TABLE users')
# print(c)
#
# # Function to register a new user
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

#for resteting your pass
def forgot_pass():
    if user:
        username = input('enter your username')
        email = input('enter your registered email: ')
        new_pass = input('enter your new pass: ')
        cursor.execute("UPDATE users SET password = ? WHERE email_id = ?" , (new_pass ,email))
        conn.commit()
        print(" new password updated successfully")
    else:
        print('wrong email entered')



while True:
    print('\nchoose one option for perform  \n1  register user \n2  login user \n3  forgot pass \n4  close ')
    user = int(input("choose one option: "))
    if user == 1:
        register()
    elif user == 2:
        login()
    elif user == 3:
        forgot_pass()
    elif user == 4:
        break
    else:
        print("❌invalid option")
