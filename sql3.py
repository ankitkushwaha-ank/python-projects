import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Insert data
name =input('give me the name:  ')
age = input('give me your age: ')
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name ,age))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# Commit changes
conn.commit()

# Retrieve and display data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()
