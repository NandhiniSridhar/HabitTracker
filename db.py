import sqlite3
import userData

#global
connection = sqlite3.connect("habits.db")
#id = 0

#database functions
def create_table():
    connection.execute('''
    CREATE TABLE habits(
        id INTEGER PRIMARY KEY,
        week INTEGER ,
        sleep INTEGER,
        study INTEGER,
        progress INTEGER,
        exercise INTEGER,
        mood INTEGER,
        stress TEXT          
    )
    ''')

def insert_to_table(input_list, week):
    # test_habits = [
    #     (0, 1, 8, 4, 1, 7, "not much"),
    #     (1, 1, 6, 2, 1, 8, "tests"),
    # ]
    
    id = 2 #test
    input_list = input_list.insert(0, week)
    input_list = input_list.insert(0, id)
    values = tuple(input_list)
    print(values)
    print(type(values))

    connection.executemany("INSERT INTO habits VALUES(?,?,?,?,?,?,?)", values)
    connection.commit()

    cur = connection.cursor()
    cur.execute("SELECT * FROM habits")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():

    habit_table = connection.execute("SELECT name FROM sqlite_master WHERE type=='table' AND name=='habits'").fetchall()
    if(habit_table == []):
        create_table()
    # else:
    #     numrows = connection.execute("SELECT COUNT(*) FROM habits")
    #     id = numrows + 1

    connection.close()
    # connection.execute("DROP TABLE habit_db")

if __name__ == "__main__":
    main()
