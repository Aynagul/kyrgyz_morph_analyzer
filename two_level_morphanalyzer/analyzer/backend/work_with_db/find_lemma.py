import sqlite3


def find_only_lemma(root):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")

        cursor.execute("select root from analyzer_allroot WHERE root = ? ", root)
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
def find_lemma_for_part_of_speech(root, word_without_punctuation):
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
            return True, word_without_punctuation, ls[1], ls[1:]
        else:
            cursor.close()
            return False, word_without_punctuation, '', []
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
def find_lemma(self, root, word_without_punctuation, cursor):

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
        self.__root = word_without_punctuation
        self.__part_of_speech = ls[1]
        self.__symbols_list = ls[1:]
        cursor.close()
        return True
    else:
        cursor.close()
        return False