import sqlite3



def find_endings(ending):
    ls = []
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        cursor.execute("select tag, priority from analyzer_endings a join analyzer_tags\
                        at on a.tagid_id = at.id WHERE name = ?", ending)
        record = cursor.fetchone()

        if record is not None:
            for i in record:
                ls.append(i)
            ls = list(dict.fromkeys(ls))
            cursor.close()
            print(ls[0])
            print(ls[1])
            return str(ls[0]), str(ls[1])
        else:
            print("ending not found in db")
            cursor.close()
            return False, False
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


