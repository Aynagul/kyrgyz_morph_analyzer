import nltk
# from exceptions import sourceModule
from analyzer.backend.analyzer.block import block_of_noun, block_of_verb, block_of_numeral, block_of_adjective, common
from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.block.common import convertTuple
from analyzer.backend.analyzer.check import check_punctuation_marks, check_special_pronouns, check_priority_of_endings, check_tags, check_vowels
from analyzer.backend.analyzer.ending_split.ending_split import ending_split
from analyzer.backend.analyzer.endings import Noun, Cases, Faces, Others, Adverb, Possessiveness, Adjectives_2, Numeral, \
    Pronoun, Verb
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.analyzer.reader import file_reader
from analyzer.backend.analyzer.result import get_all_info
from analyzer.backend.work_with_db.find_lemma import find_lemma
from analyzer.backend.work_with_db.find_lemma import find_only_lemma
from analyzer.backend.work_with_db.find_lemma import find_lemma_for_part_of_speech
from analyzer.backend.work_with_db.find_endings import find_endings
from analyzer.backend.analyzer import noun_analyzer
from analyzer.backend.analyzer import verb_analyzer
from analyzer.backend.analyzer import numeral_analyzer
from analyzer.backend.analyzer import adjective_analyzer

import sqlite3



is_first_letter_upper = False
class Word:
    __original_word = ''
    __change_word = ''
    __root = ''
    __number = 0
    __root_from_the_end = ''
    __all_info = ''
    __part_of_speech = ''
    __symbols = {}
    __symbols_list = []
    __result_text = ''
    __first_punctuation_mark = ''
    __last_punctuation_mark = ''
    __word_without_punctuation = ''
    __wrong_priority = False
    __is_like_a_noun = False
    __last_vowel_of_lemma = ''
    __affix = ''
    def __init__(self, word):
        self.__original_word = word
        self.__word_without_punctuation = word.lower()
        self.__change_word = word.lower()
        self.__symbols = {}
        self.__symbols_list = []

    def find_root(self, new_word):
        new_word = (new_word, )

        is_found, self.__root = find_only_lemma(new_word)
        if is_found:
            is_found, self.__word_without_punctuation, self.__part_of_speech, self.__symbols_list \
                    = find_lemma_for_part_of_speech(new_word, self.__word_without_punctuation)
            if is_found:
                self.__last_vowel_of_lemma = check_vowels.get_last_vowel(new_word)
                self.__affix = common.strip_affix_from_word(self.__word_without_punctuation, convertTuple(new_word))
                return True
            else:
                return False




    def find_root_from_the_end(self, new_word):
        new_word = (new_word,)

        is_found, self.__root = find_only_lemma(new_word)
        if is_found:
            self.__symbols_list.reverse()
            list = self.__symbols_list.copy()
            self.__symbols_list.clear()
            is_found, self.__word_without_punctuation, self.__part_of_speech, self.__symbols_list \
                = find_lemma_for_part_of_speech(new_word, self.__word_without_punctuation)
            self.__symbols_list = self.__symbols_list + list
            self.__symbols_list.reverse()
            if is_found:
                return True
            else:
                return False
        '''if (res := file_reader.read_file(new_word)) != 'none':
            self.__part_of_speech = res[0]
            self.__symbols_list.reverse()
            list = self.__symbols_list.copy()
            self.__symbols_list.clear()
            self.__symbols_list = res + list
            self.__symbols_list.reverse()
            self.__root = new_word
            return True
        else:
            return False'''
    def word_analyze(self, word):
        new_word = self.change_word[:1]
        self.set_change_word(self.__change_word[1:])
        for ch in self.change_word:
            if self.find_root(new_word):
                pass
            new_word += ch
        if not check_vowels.check_ending_vowels(self.__last_vowel_of_lemma, self.__affix):
            return 'Wrong'

        #word = analyzer.sourceModule.replace_letter(word)
        words = nltk.word_tokenize(word)
        try:
            syllables_of_words = ending_split(words)
        except:
            return 'Wrong'


        ending_list = syllables_of_words
        ending_list.reverse()
        new_list = list(ending_list)
        ending_priority = 8
        print(new_list)
        for ending in ending_list:
            str_ending = listToString(ending)
            print("Ending: {0}".format(str_ending))
            index = new_list.index(ending)

            if self.part_of_speech == 'n':
                str, new_list, new_word, ending_priority = noun_analyzer.noun_analyzer(self, str_ending, index, new_list,
                                                                                       ending, ending_list, new_word, ending_priority,
                                                                                       self.__symbols_list, self.__symbols)

                if str == sourceModule.str_continue:
                    continue
                elif str == sourceModule.str_break:
                    break
                if self.find_root_from_the_end(new_word):
                    break
                else:
                    new_list.reverse()
                    continue
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'v':
                str, new_list, new_word, ending_priority = verb_analyzer.verb_analyzer(self, str_ending, index,
                                                                                       new_list,
                                                                                       ending, ending_list, new_word,
                                                                                       ending_priority,
                                                                                       self.__symbols_list,
                                                                                       self.__symbols)

                if str == sourceModule.str_continue:
                    continue
                elif str == sourceModule.str_break:
                    break
                if self.find_root_from_the_end(new_word):
                    break
                else:
                    new_list.reverse()
                    continue

# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'num' or self.__word_without_punctuation in sourceModule.num_word_special:
                str, new_list, new_word, ending_priority = numeral_analyzer.numeral_analyzer(self, str_ending, index,
                                                                                       new_list,
                                                                                       ending, ending_list, new_word,
                                                                                       ending_priority,
                                                                                       self.__symbols_list,
                                                                                       self.__symbols)

                if str == sourceModule.str_continue:
                    continue
                elif str == sourceModule.str_break:
                    break
                if self.find_root_from_the_end(new_word):
                    break
                else:
                    new_list.reverse()
                    continue


# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adj":
                str, new_list, new_word, ending_priority = adjective_analyzer.adjective_analyzer(self, str_ending, index,
                                                                                             new_list,
                                                                                             ending, ending_list,
                                                                                             new_word,
                                                                                             ending_priority,
                                                                                             self.__symbols_list,
                                                                                             self.__symbols)

                if str == sourceModule.str_continue:
                    continue
                elif str == sourceModule.str_break:
                    break
                if self.find_root_from_the_end(new_word):
                    break
                else:
                    new_list.reverse()
                    continue
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "prn":
                if (symbol := Cases.get_info_cases(ending)) != 'none':
                    new_list, new_word = common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := Faces.get_info_faces(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        common.faces(index, new_list, symbol, str_ending, self.__symbols_list, self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

                elif (symbol := Others.get_info_other(ending)) != 'none':
                    new_list, new_word = common.common(self, index, new_list, symbol, str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := Possessiveness.get_info_possessive(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        common.possessiveness(index, new_list, symbol, str_ending, self.__symbols_list,
                                                      self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                else:
                    new_list, index, last_letter, str = \
                        common.common_exception_1(new_list, str_ending)
                    # for posessiveness_general (ныкы) итд
                    if ending in sourceModule.half_of_ending_for_general_possessiveness and new_list[
                        index - 1] in sourceModule.posessiveness_general:
                        new_list, index, ending, ending_list = common.common_exception_2(index, new_list,
                                                                                                 str_ending,
                                                                                                 ending_list, str)
                        continue
                    elif len(ending) == 2 and last_letter in sourceModule.special_vowel:
                        if not self.__symbols:  # px3sp only
                            new_list, index, ending, ending_list, index2 = common.common_exception_3 \
                                (index, new_list, str_ending, ending_list, str)
                            if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                new_list, index, new_word = common.common_exception_4 \
                                    (self, new_list, symbol, last_letter, str)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in Possessiveness.posessiveness_2st_sg_politely or key in Possessiveness.posessiveness_1st_pl or key \
                                        in Possessiveness.posessiveness_2st_pl:
                                    is_px3sp = False
                                    index, new_list, last_letter, ending, self.__symbols, ending_list = \
                                        common.common_exception_5(index, new_list, last_letter, ending,
                                                                          self.__symbols, ending_list, str)
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list, ending_list = common.common_exception_6(index, new_list, ending,
                                                                                          ending_list, str)
                                if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    new_list, new_word = common.common_exception_7(self, symbol, new_list,
                                                                                           last_letter, str)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        new_word = listToString(new_list)
                                        if self.find_root_from_the_end(new_word):
                                            break
                                        else:
                                            continue
                            else:  # ыңар, ыбыз, ыңыз
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    new_word = listToString(new_list)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        continue
                    # for px1sg(ым) and px2sg(ың)
                    else:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        try:
                            new_list, ending_list = common.common_exception_8(index, new_list, ending,
                                                                                      ending_list, str)
                        except:
                            new_list, ending_list = common.common_exception_9(index, new_list, ending,
                                                                                      ending_list, str)
                        str = listToString(new_list[index])
                        if (symbol := Possessiveness.get_info_possessive(str)) != 'none':
                            new_list, new_word = common.common_exception_10(self, new_list, symbol, str)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adv":
                # adverb don't write with endings
                self.__wrong_priority = True
                break
            elif self.part_of_speech in sourceModule.POS_without_ending_tags:
                #these part of speeches don't write with endings
                self.__wrong_priority = True
                break

        return 'end'
    def search_only_numeral(self, text):
        if number := Numeral.get_info_numeral_root(nltk.word_tokenize(text)) != 'none':
            return number
        else:
            return '[' + str(text) + ']'

    def search_word_db_for_text(self,word):
        if len(word) > 33:
            self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
            return self.__result_text
        if word[-1] in sourceModule.all_punctuation_marks and word[0] not in sourceModule.all_punctuation_marks:
            self.__last_punctuation_mark, self.__word_without_punctuation = check_punctuation_marks.situation_1(word)

        elif word[-1] not in sourceModule.all_punctuation_marks and word[0] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__word_without_punctuation = check_punctuation_marks.situation_2(word)
        elif word[0] in sourceModule.all_punctuation_marks and word[-1] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__last_punctuation_mark, self.__word_without_punctuation = \
                check_punctuation_marks.situation_3(word)
        if self.__word_without_punctuation.isnumeric():
            self.__root, self.__symbols_list, self.__part_of_speech = block_of_numeral.if_is_digit(self.__symbols_list,
                                                                                                      self.__word_without_punctuation)
            self.set_all_info()
            return self.__all_info

        elif self.__word_without_punctuation.lower() in sourceModule.special_pronoun:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := Pronoun.get_info_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.is_sg_or_pl(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.cases_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                self.__root = check_special_pronouns.check_pronouns(self, symbol, self.__word_without_punctuation.lower())
            self.set_all_info()
            return self.__all_info


        else:
            root = self.__word_without_punctuation.lower()
            is_found = False
            try:
                sqliteConnection = sqlite3.connect('db.sqlite3')
                cursor = sqliteConnection.cursor()
                is_found, self.__root, self.__part_of_speech, self.__symbols_list = find_lemma(root, self.__word_without_punctuation, cursor)
                if is_found:
                    self.set_all_info()
                    return self.__all_info
                else:
                    cursor.close()

            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()

            if not is_found:
                print("no")
                try:
                    end = self.word_analyze(self.__word_without_punctuation.lower())
                    if end == 'end':
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        self.__part_of_speech = ''
                        self.__symbols_list = []
                        self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                        return "I dont know this word"
                except:

                    self.__part_of_speech = ''
                    self.__symbols_list = []
                    self.__result_text = '['+str(self.__word_without_punctuation)+']' + self.__last_punctuation_mark
                    return self.__original_word

    def search_word_db_for_word(self,word):

        if self.__word_without_punctuation.isnumeric():
            self.__root, self.__symbols_list, self.__part_of_speech = block_of_numeral.if_is_digit(self.__symbols_list,
                                                                                                      self.__word_without_punctuation)
            self.set_all_info()
            return self.__all_info

        elif self.__word_without_punctuation.lower() in sourceModule.special_pronoun:
            self.__root = self.__word_without_punctuation
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := Pronoun.get_info_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.is_sg_or_pl(self.__word_without_punctuation.lower())) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.cases_pronoun_root(self.__word_without_punctuation.lower())) != 'none':
                self.__root = check_special_pronouns.check_pronouns(self, symbol, self.__word_without_punctuation.lower())
            self.set_all_info()
            return self.__all_info
        elif self.__word_without_punctuation.lower() in sourceModule.num_word_special:
            self.__part_of_speech = 'num'
            self.set_symbols_list('num')
            self.__root, self.__symbols_list = Numeral.check_numerals(self, self.__word_without_punctuation.lower(), self.__symbols_list)

            self.set_all_info()
            return self.__all_info


        else:
            root = (self.__word_without_punctuation.lower(), )
            is_found = False
            try:
                sqliteConnection = sqlite3.connect('db.sqlite3')
                cursor = sqliteConnection.cursor()
                is_found, self.__root, self.__part_of_speech, self.__symbols_list = find_lemma(root, self.__word_without_punctuation, cursor)
                if is_found:
                    self.set_all_info()
                    return self.__all_info
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()

            if not is_found:
                print("no")
                try:
                    end = self.word_analyze(self.__word_without_punctuation.lower())
                    if end == 'end':
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        self.__part_of_speech = ''
                        self.__symbols_list = []
                        self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                        return "I dont know this word"
                except:
                    print('not analyzed')
                    self.__part_of_speech = ''
                    self.__symbols_list = []
                    self.__result_text = '['+str(self.__word_without_punctuation)+']' + self.__last_punctuation_mark
                    return self.__original_word



    def ending_analyze(ending):
        pass
    @property
    def original_word(self):
        return self.__original_word

    @property
    def word_without_punctuation(self):
        return self.__word_without_punctuation

    @property
    def part_of_speech(self):
        return self.__part_of_speech


    @property
    def root(self):
        return self.__root

    @property
    def first_punctuation_mark(self):
        return self.__first_punctuation_mark

    @property
    def last_punctuation_mark(self):
        return self.__last_punctuation_mark
    @property
    def result_text(self):
        return self.__result_text
    @property
    def number(self):
        return self.__number
    @property
    def root_from_the_end(self):
        return self.__root_from_the_end
    @property
    def all_info(self):
        return self.__all_info

    @property
    def change_word(self):
        return self.__change_word

    @property
    def symbols_list(self):
        return self.__symbols_list
    @property
    def symbols(self):
        self.__symbols = dict(reversed(list(self.__symbols.items())))
        return self.__symbols
    def get_symbols_list(self):
        return self.__symbols_list.reverse()
    def set_number(self, number):
        self.__number = number
    def set_part_of_speech(self, part_of_speech):
        self.__part_of_speech = part_of_speech
    def set_root(self, root):
        self.__root = root
    def set_root_from_the_end(self, root):
        self.__root_from_the_end = root
    def set_change_word(self, change_word):
        self.__change_word = change_word
    def set_symbol(self, symbol, ending):
        self.__symbols[ending] = symbol
    def set_symbols_list(self, symbol):
        self.__symbols_list.append(symbol)
    def set_all_info(self):
        self.__wrong_priority, self.__symbols_list = check_tags.check_tags(self.__symbols_list, self.__wrong_priority)
        self.__result_text, self.__all_info, self.__symbols_list, self.__symbols = get_all_info.get_info(self, self.__symbols_list, self.__symbols,
                                                           self.__root,
                                                           self.__first_punctuation_mark,
                                                           self.__word_without_punctuation,
                                                           self.__last_punctuation_mark,
                                                            self.__wrong_priority)
        print(self.__result_text)

        self.__symbols_list = [i for i in self.__symbols_list if i is not None]
        self.__symbols_list = list(dict.fromkeys(self.__symbols_list))



