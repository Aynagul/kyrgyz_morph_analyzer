import sqlite3


def find_only_lemma(root):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        cursor.execute("select root from analyzer_allroot WHERE root = ?", root)
        record = cursor.fetchone()
        if record:
            cursor.close()
            return True, record[0]
        else:
            cursor.close()
            return False, ''
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def find_lemma_for_part_of_speech(root):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        cursor.execute("select root, part_of_speech, tag from analyzer_allroot a \
                                           left join analyzer_partofspeech ap on ap.id = a.part_of_speech_id \
                                           left join analyzer_allroot_tag aat on a.id = aat.allroot_id \
                                           left join analyzer_tags at on at.id = aat.tags_id \
                                           where root = ?", root)
        record = cursor.fetchall()
        if not record == []:
            ls = []
            for i in record:
                for j in i:
                    ls.append(j)
            ls = list(dict.fromkeys(ls))
            cursor.close()
            return True, ls[1], ls[1:]
        else:
            cursor.close()
            return False, '', []
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def find_lemma(root, word_without_punctuation, cursor):

    print("Database created and Successfully Connected to SQLite")
    part_of_speech = ''
    symbols_list = []
    cursor.execute("select root, part_of_speech, tag from analyzer_allroot a \
                                       left join analyzer_partofspeech ap on ap.id = a.part_of_speech_id \
                                       left join analyzer_allroot_tag aat on a.id = aat.allroot_id \
                                       left join analyzer_tags at on at.id = aat.tags_id \
                                       where root = ?", root)
    record = cursor.fetchall()
    print('record')
    print(record)
    tag_id = [1,2,3,4]
    tag = 0
    if not record == []:
        ls = []
        for i in record:
            for j in i:
                if j in tag_id:
                    tag = j
                ls.append(j)
        ls = list(dict.fromkeys(ls))
        root = word_without_punctuation
        part_of_speech = ls[1]
        symbols_list = ls[1:]
        cursor.close()
        return True, root, part_of_speech, symbols_list
    else:
        cursor.close()
        return False, root, part_of_speech, symbols_list


def is_lemma_in_db(root):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        cursor.execute("select root, part_of_speech, tag from analyzer_allroot a \
                                           left join analyzer_partofspeech ap on ap.id = a.part_of_speech_id \
                                           left join analyzer_allroot_tag aat on a.id = aat.allroot_id \
                                           left join analyzer_tags at on at.id = aat.tags_id \
                                           where root = ?", root)
        record = cursor.fetchall()
        if not record == []:
            cursor.close()
            return True
        else:
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()