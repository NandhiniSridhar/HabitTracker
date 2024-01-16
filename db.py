import sqlite3
#print(sqlite3.sqlite_version)

connection = sqlite3.connect("habits.db")

# connection.execute('''
# CREATE TABLE habit_db(
#     id INTEGER PRIMARY KEY,
#     week INTEGER ,
#     sleep INTEGER,
#     study INTEGER,
#     exercise INTEGER,
#     mood INTEGER,
#     stress TEXT          
# )
# ''')

test_habits = [(0, 1, 8, 4, 1, 7, "not much"), (1, 1, 6, 2, 1, 8, "tests")]
connection.executemany("INSERT INTO habit_db VALUES(?,?,?,?,?,?,?)", test_habits)
connection.commit()

cur = connection.cursor()
cur.execute("SELECT * FROM habit_db")
rows = cur.fetchall()
for row in rows:
    print(row)
connection.close()
