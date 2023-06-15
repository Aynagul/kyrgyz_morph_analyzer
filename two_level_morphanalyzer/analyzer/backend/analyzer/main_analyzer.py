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
from analyzer.backend.work_with_db.find_lemma import find_only_lemma, find_lemma_for_text
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
    __lower_case_word = ''
    __changed_word = ''
    __root = ''
    __number = 0
    __root_from_the_end = ''
    __all_info = ''
    __part_of_speech = ''
    __part_of_speech_list = []
    __symbols = {}
    __symbols_str = ''
    __symbols_list = []
    __symbols_list_str = ''
    __symbols_list_for_2_lemma = [[]]
    __result_text = ''
    __first_punctuation_mark = ''
    __last_punctuation_mark = ''
    __word_without_punctuation = ''
    __wrong_priority = False
    __is_like_a_noun = False
    __last_vowel_of_lemma = ''
    __affix = ''
    __is_homonym = False
    def __init__(self, word):
        self.__original_word = word
        self.__word_without_punctuation = word
        self.__lower_case_word = word.lower()
        self.__symbols = {}
        self.__symbols_list = []

    def find_root(self, new_word):
        new_word = (new_word, )

        is_found, self.__root = find_only_lemma(new_word)
        if is_found:
            is_found, self.__part_of_speech, self.__symbols_list \
                    = find_lemma_for_part_of_speech(new_word)
            if is_found:
                self.__last_vowel_of_lemma = check_vowels.get_last_vowel(new_word)
                self.__affix = common.strip_affix_from_word(self.__lower_case_word, convertTuple(new_word))

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
            is_found, self.__part_of_speech, self.__symbols_list \
                = find_lemma_for_part_of_speech(new_word)
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
        new_word = word[:1]
        self.set_changed_word(word[1:])
        for ch in self.__changed_word:
            if self.find_root(new_word):
                pass
            new_word += ch
        if not check_vowels.check_ending_vowels(self.__last_vowel_of_lemma, self.__affix):
            print('wrong vowel in ending')
            return False

        #word = analyzer.sourceModule.replace_letter(word)
        words = nltk.word_tokenize(word)
        try:
            syllables_of_words = ending_split(words)
        except:
            return False


        ending_list = syllables_of_words
        ending_list.reverse()
        new_list = list(ending_list)
        ending_priority = 8
        print(new_list)
        print(self.part_of_speech)
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
                str, new_list, new_word, ending_priority = noun_analyzer.noun_analyzer(self, str_ending, index,
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
            elif self.part_of_speech == "adv":
                # adverb don't write with endings
                self.__wrong_priority = True
                break
            elif self.part_of_speech in sourceModule.POS_without_ending_tags:
                #these part of speeches don't write with endings
                self.__wrong_priority = True
                break
            elif self.__part_of_speech == '':
                return False

        return True
    def search_only_numeral(self, text):
        if number := Numeral.get_info_numeral_root(nltk.word_tokenize(text)) != 'none':
            return number
        else:
            return '[' + str(text) + ']'

    def search_word_db_for_text(self,word):
        if len(word.__original_word) > 33:
            self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
            return self.__result_text

        if word.__original_word[-1] in sourceModule.all_punctuation_marks and word.__original_word[
            0] not in sourceModule.all_punctuation_marks:
            self.__last_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = check_punctuation_marks.situation_1(
                word.__original_word)
            print(self.__word_without_punctuation)
            print(self.__last_punctuation_mark)
        elif word.__original_word[-1] not in sourceModule.all_punctuation_marks and word.__original_word[
            0] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = check_punctuation_marks.situation_2(
                word.__original_word)
        elif word.__original_word[0] in sourceModule.all_punctuation_marks and word.__original_word[
            -1] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__last_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = \
                check_punctuation_marks.situation_3(word.__original_word)

        if self.__lower_case_word.isnumeric():
            self.__root, self.__symbols_list, self.__part_of_speech = block_of_numeral.if_is_digit(self.__symbols_list,
                                                                                                   self.__word_without_punctuation)
            self.set_all_info()
            return self.__all_info
        if self.__lower_case_word in sourceModule.special_pronoun:
            self.__root = self.__lower_case_word
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := Pronoun.get_info_pronoun_root(self.__lower_case_word)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.is_sg_or_pl(self.__lower_case_word)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.cases_pronoun_root(self.__lower_case_word)) != 'none':
                self.__root = check_special_pronouns.check_pronouns(self, symbol, self.__lower_case_word)
            self.set_all_info()
            return self.__all_info
        elif self.__lower_case_word in sourceModule.num_word_special:
            self.__part_of_speech = 'num'
            self.set_symbols_list('num')
            self.__root, self.__symbols_list = Numeral.check_numerals(self, self.__lower_case_word, self.__symbols_list)
            self.set_all_info()
            return self.__all_info
        elif self.__lower_case_word in sourceModule.adj_word_special:
            self.__part_of_speech = 'adj'
            self.set_symbols_list('adj')
            self.__root, self.__symbols_list = Adjectives_2.check_adjectives(self, self.__lower_case_word,
                                                                             self.__symbols_list)
            self.set_all_info()
            return self.__all_info

        else:

            root = (self.__lower_case_word,)
            is_found = False
            try:
                sqliteConnection = sqlite3.connect('db.sqlite3')
                cursor = sqliteConnection.cursor()
                is_found, self.__root, self.__part_of_speech, self.__symbols_list = \
                    find_lemma_for_text(root, self.__lower_case_word, cursor)
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
                    is_correct_analyze = self.word_analyze(self.__lower_case_word)
                    if is_correct_analyze:
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        self.__part_of_speech = ''
                        self.__symbols_list = []
                        self.__result_text = self.__first_punctuation_mark + '[' + str(
                            self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                        return "I dont know this word"
                except:
                    print('not analyzed')
                    self.__part_of_speech = ''
                    self.__symbols_list = []
                    self.__result_text = self.__first_punctuation_mark + '[' + str(
                        self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                    return self.__original_word

    def search_word_db_for_word(self,word):
        if len(word.__original_word) > 33:
            self.__result_text = '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
            return self.__result_text

        if word.__original_word[-1] in sourceModule.all_punctuation_marks and word.__original_word[0] not in sourceModule.all_punctuation_marks:
            self.__last_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = check_punctuation_marks.situation_1(word.__original_word)
            print(self.__word_without_punctuation)
            print(self.__last_punctuation_mark)
        elif word.__original_word[-1] not in sourceModule.all_punctuation_marks and word.__original_word[0] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = check_punctuation_marks.situation_2(word.__original_word)
        elif word.__original_word[0] in sourceModule.all_punctuation_marks and word.__original_word[-1] in sourceModule.all_punctuation_marks:
            self.__first_punctuation_mark, self.__last_punctuation_mark, self.__word_without_punctuation, self.__lower_case_word = \
                check_punctuation_marks.situation_3(word.__original_word)

        if self.__lower_case_word.isnumeric():
            self.__root, self.__symbols_list, self.__part_of_speech = block_of_numeral.if_is_digit(self.__symbols_list,
                                                                                                      self.__word_without_punctuation)
            self.set_all_info()
            return self.__all_info
        if self.__lower_case_word in sourceModule.special_pronoun:
            self.__root = self.__lower_case_word
            self.__part_of_speech = 'prn'
            self.set_symbols_list('prn')
            if (symbol := Pronoun.get_info_pronoun_root(self.__lower_case_word)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.is_sg_or_pl(self.__lower_case_word)) != 'none':
                self.set_symbols_list(symbol)
            if (symbol := Pronoun.cases_pronoun_root(self.__lower_case_word)) != 'none':
                self.__root = check_special_pronouns.check_pronouns(self, symbol, self.__lower_case_word)
            self.set_all_info()
            return self.__all_info
        elif self.__lower_case_word in sourceModule.num_word_special:
            self.__part_of_speech = 'num'
            self.set_symbols_list('num')
            self.__root, self.__symbols_list = Numeral.check_numerals(self, self.__lower_case_word, self.__symbols_list)
            self.set_all_info()
            return self.__all_info
        elif self.__lower_case_word in sourceModule.adj_word_special:
            self.__part_of_speech = 'adj'
            self.set_symbols_list('adj')
            self.__root, self.__symbols_list = Adjectives_2.check_adjectives(self, self.__lower_case_word, self.__symbols_list)
            self.set_all_info()
            return self.__all_info

        else:

            root = (self.__lower_case_word, )
            is_found = False
            try:
                sqliteConnection = sqlite3.connect('db.sqlite3')
                cursor = sqliteConnection.cursor()
                is_found, self.__root, self.__part_of_speech_list, self.__symbols_list_for_2_lemma, self.__is_homonym = \
                    find_lemma(root, self.__lower_case_word, cursor)
                if is_found:
                    self.set_all_info_for_lemma_only()
                    return self.__all_info
            except sqlite3.Error as error:
                print("Error while connecting to sqlite", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()

            if not is_found:
                print("no")
                try:
                    is_correct_analyze = self.word_analyze(self.__lower_case_word)
                    if is_correct_analyze:
                        self.__symbols_list.reverse()
                        self.set_all_info()
                        return self.__all_info
                    else:
                        self.__part_of_speech = ''
                        self.__symbols_list = []
                        self.__result_text = self.__first_punctuation_mark + '[' + str(self.__word_without_punctuation) + ']' + self.__last_punctuation_mark
                        return "I dont know this word"
                except:
                    print('not analyzed')
                    self.__part_of_speech = ''
                    self.__symbols_list = []
                    self.__result_text = self.__first_punctuation_mark + '['+str(self.__word_without_punctuation)+']' + self.__last_punctuation_mark
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
    def symbols_list_for_2_lemma(self):
        return self.__symbols_list_for_2_lemma

    @property
    def part_of_speech_list(self):
        return self.__part_of_speech_list


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
    def symbols_list_str(self):
        return self.__symbols_list_str

    @property
    def symbols_str(self):
        return self.__symbols_str
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
    def is_homonym(self):
        return self.__is_homonym


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
    def set_changed_word(self, changed_word):
        self.__changed_word = changed_word
    def set_symbol(self, symbol, ending):
        self.__symbols[ending] = symbol
    def set_symbols_list(self, symbol):
        self.__symbols_list.append(symbol)
    def set_all_info(self):
        self.__wrong_priority, self.__symbols_list = check_tags.check_tags(self.__symbols_list, self.__wrong_priority)
        self.__result_text, self.__all_info, self.__symbols_list, self.__symbols, self.__symbols_list_str, self.__symbols_str = \
            get_all_info.get_info(self, self.__symbols_list, self.__symbols,
                                                           self.__root,
                                                           self.__first_punctuation_mark,
                                                           self.__lower_case_word,
                                                           self.__last_punctuation_mark,
                                                            self.__wrong_priority,
                                                            self.__word_without_punctuation)
        self.__part_of_speech = '<' + self.__part_of_speech + '>'
        print(self.__result_text)
        self.__symbols_list = [i for i in self.__symbols_list if i is not None]
        self.__symbols_list = list(dict.fromkeys(self.__symbols_list))
    def set_all_info_for_lemma_only(self):
        symbols_text = ''
        ending_symbols = []
        tag_str = ''
        self.__part_of_speech = self.__part_of_speech_list[0]
        self.__symbols_list = self.__symbols_list_for_2_lemma[0]
        print(self.__symbols_list)
        if self.__is_homonym:
            def_symbols_text = ''
            def_symbols_text2 = ''

            self.__part_of_speech = '<'+self.__part_of_speech + '>' + '; '+'<'+self.__part_of_speech_list[1]+'>'
            for sym in list(dict.fromkeys(self.__symbols_list)):
                print(sym)
                def_symbols_text = def_symbols_text + '<' + str(sym) + '>'
            for sym in list(dict.fromkeys(self.__symbols_list_for_2_lemma[1])):
                def_symbols_text2 = def_symbols_text2 + '<' + str(sym) + '>'
            self.__symbols_list_str = def_symbols_text + '; ' + def_symbols_text2
            self.__result_text = str(self.__first_punctuation_mark) + str(self.__word_without_punctuation) + \
                                 "/" + str(self.__root)  + def_symbols_text + str(self.__last_punctuation_mark) + '\n' + \
                                 str(self.__word_without_punctuation) + '/' + str(self.__root) + def_symbols_text2

            print(self.__result_text)
            self.__symbols_list = [i for i in self.__symbols_list if i is not None]
        else:
            self.__part_of_speech = '<' + self.__part_of_speech + '>'
            def_symbols_text = ''
            for sym in list(dict.fromkeys(self.__symbols_list)):
                def_symbols_text = def_symbols_text + '<' + str(sym) + '>'
            self.__symbols_list_str = def_symbols_text
            self.__result_text = str(self.__first_punctuation_mark) + str(self.__word_without_punctuation) + \
                          "/" + str(self.__root) + def_symbols_text + str(self.__last_punctuation_mark)

            print(self.__result_text)
            self.__symbols_list = [i for i in self.__symbols_list if i is not None]
            self.__symbols_list = list(dict.fromkeys(self.__symbols_list))


