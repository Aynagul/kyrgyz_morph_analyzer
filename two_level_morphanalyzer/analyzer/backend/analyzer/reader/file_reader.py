import csv
import sys
sys.path.append('analyzer/backend/analyzer/csv_files/noun.csv')
def read_file(word):
    with open('analyzer/backend/analyzer/csv_files/new_words.csv', encoding='utf-8') as r_file2:
        file_reader2 = csv.reader(r_file2, delimiter="\n")
        flag1 = False
        for row in file_reader2:
            symbolss = row[0].split('; ')
            if word == symbolss[0]:
                flag1 = True
                symbols_arr = symbolss[1:]
                break
        if flag1:
            return symbols_arr
        else:
            with open('analyzer/backend/analyzer/csv_files/All.csv', encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter="\n")
                flag = False
                for row in file_reader:
                    symbolss = row[0].split(';')
                    if word == symbolss[0]:
                        flag = True
                        symbols_arr = symbolss[1:]
                        break
                if flag:
                    return symbols_arr
                else:
                    return "none"

