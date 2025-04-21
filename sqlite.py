import sqlite3
conn = sqlite3.connect('first.db')

# creating tables
conn.execute('''
create table students(
std_id INT AUTO_INCREMENT PRIMARY KEY,
std_name VARCHAR(50),
std_email VARCHAR(20)
)
''')
conn.close()

# inserting data in database
ins = ('''
insert into students (std_name ,std_email) values ('Ankit','ankitrajaryan247@gmail.com')

''')
conn.execute(ins)
conn.commit()
conn.close()

#for printing the database in terminal
data = conn.execute('SELECT * FROM students')
for n in data:
    print(n)