import sqlite3
import userData
#print(sqlite3.sqlite_version)

connection = sqlite3.connect("habits.db")

habit_table = connection.execute("SELECT name FROM sqlite_master WHERE type=='table' AND name=='habits'").fetchall()
if(habit_table == []):
    connection.execute('''
    CREATE TABLE habits(
        id INTEGER PRIMARY KEY,
        week INTEGER ,
        sleep INTEGER,
        study INTEGER,
        exercise INTEGER,
        mood INTEGER,
        stress TEXT          
    )
    ''')

test_habits = [
    (0, 1, 8, 4, 1, 7, "not much"),
    (1, 1, 6, 2, 1, 8, "tests"),
]
connection.executemany("INSERT INTO habits VALUES(?,?,?,?,?,?,?)", test_habits)
connection.commit()

cur = connection.cursor()
cur.execute("SELECT * FROM habits")
rows = cur.fetchall()
for row in rows:
    print(row)

#will probably take this line out later- figure out how to keep database and just keep updating it
#connection.execute("DROP TABLE habits")
connection.close()

# connection.execute("DROP TABLE habit_db")