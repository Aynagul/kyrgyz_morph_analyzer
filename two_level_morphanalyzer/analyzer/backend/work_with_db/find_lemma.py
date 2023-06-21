import sqlite3
from analyzer.backend.analyzer.exceptions import sourceModule
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
    part_of_speech = []
    symbols_list = []
    is_homonym = False
    cursor.execute("select root, part_of_speech, tag from analyzer_allroot a \
                                       left join analyzer_partofspeech ap on ap.id = a.part_of_speech_id \
                                       left join analyzer_allroot_tag aat on a.id = aat.allroot_id \
                                       left join analyzer_tags at on at.id = aat.tags_id \
                                       where root = ?", root)
    record = cursor.fetchall()

    pos_tag = []
    tag_sets = {''}
    if not record == []:
        first_lemma = []
        second_lemma = []
        for i in record:
            for j in i:
                pos_tag.append(j)
                if j in sourceModule.POS:
                    tag_sets.add(j)
                if len(tag_sets) > 2:
                    #print('homonym')
                    is_homonym = True
                    second_lemma.append(j)
                else:
                    first_lemma.append(j)



        first_lemma = list(dict.fromkeys(first_lemma))
        print('first')
        print(first_lemma)
        print('second')
        print(second_lemma)
        first_lemma.remove(word_without_punctuation.lower())
        first_lemma = [i for i in first_lemma if i is not None]
        if is_homonym:
            second_lemma = list(dict.fromkeys(second_lemma))
            if word_without_punctuation.lower() in second_lemma:
                second_lemma.remove(word_without_punctuation.lower())
            second_lemma = [i for i in second_lemma if i is not None]
            root = word_without_punctuation
            part_of_speech.append(first_lemma[0])
            symbols_list.append(first_lemma[0:])
            part_of_speech.append(second_lemma[0])
            symbols_list.append(second_lemma[0:])
            cursor.close()
            return True, root, part_of_speech, symbols_list, is_homonym
        else:
            first_lemma = list(dict.fromkeys(first_lemma))
            root = word_without_punctuation
            part_of_speech.append(first_lemma[0])
            symbols_list.append(first_lemma[0:])
            cursor.close()
            return True, root, part_of_speech, symbols_list, is_homonym
    else:
        cursor.close()
        return False, root, part_of_speech, symbols_list, is_homonym

def find_lemma_for_text(root, word_without_punctuation, cursor):
    print("Database created and Successfully Connected to SQLite")
    part_of_speech = []
    symbols_list = []
    cursor.execute("select root, part_of_speech, tag from analyzer_allroot a \
                                           left join analyzer_partofspeech ap on ap.id = a.part_of_speech_id \
                                           left join analyzer_allroot_tag aat on a.id = aat.allroot_id \
                                           left join analyzer_tags at on at.id = aat.tags_id \
                                           where root = ?", root)
    record = cursor.fetchall()
    first_lemma = []
    pos_tag = []
    tag_sets = {''}
    if not record == []:

        for i in record:
            for j in i:
                pos_tag.append(j)
                if j in sourceModule.POS:
                    tag_sets.add(j)
                if len(tag_sets) > 2:
                    # print('homonym')
                    break
                else:
                    first_lemma.append(j)

        first_lemma = list(dict.fromkeys(first_lemma))
        first_lemma = [i for i in first_lemma if i is not None]
        root = word_without_punctuation
        cursor.close()
        return True, root, first_lemma[1], first_lemma[1:]
    else:
        cursor.close()
        return False, root, '', []
def is_lemma_in_db(root):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Database created and Successfully Connected to SQLite")
        cursor.execute("select root from analyzer_allroot WHERE root = ?", root)
        record = cursor.fetchone()
        if record:
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