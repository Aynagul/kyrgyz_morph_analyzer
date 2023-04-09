import nltk
# from exceptions import sourceModule
from analyzer.backend.analyzer.block import block_of_noun, block_of_verb, block_of_numeral, block_of_adjective, common
from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.block.common import convertTuple
from analyzer.backend.analyzer.check import check_punctuation_marks, check_special_pronouns, check_priority_of_endings
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
    def __init__(self, word):
        self.__original_word = word
        self.__word_without_punctuation = word
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
        #word = analyzer.sourceModule.replace_letter(word)
        words = nltk.word_tokenize(word)
        try:
            syllables_of_words = ending_split(words)
        except:
            return 'Wrong'
        new_word = self.change_word[:1]
        self.set_change_word(self.__change_word[1:])
        for ch in self.change_word:
            if self.find_root(new_word):
                pass
            new_word += ch
        ending_list = syllables_of_words
        ending_list.reverse()
        new_list = list(ending_list)
        ending_priority = 8
        for ending in ending_list:
            str_ending = listToString(ending)
            print("Ending: {0}".format(str_ending))
            index = new_list.index(ending)

            if self.part_of_speech == 'n':
                print('noun block')
                str_ending = (str_ending, )
                symbol, priority = find_endings(str_ending)
                if symbol:
                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(ending_priority, priority)
                    if is_correct_priority:
                        if symbol in sourceModule.faces:
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                            common.faces(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list, self.__symbols)

                        elif symbol in sourceModule.case:
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol in sourceModule.possessiveness:
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                                common.possessiveness(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list,
                                                      self.__symbols)
                        elif symbol == sourceModule.plural or symbol == sourceModule.ques or symbol == sourceModule.agent_noun \
                                or symbol == sourceModule.negative:
                            new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                                common.common_exception_11(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list,
                                             self.__symbols, ending_priority)
                            #new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))

                        elif symbol == 'opt':
                            # for posessiveness_general (ныкы) итд
                            ending_priority = 3
                            new_list, index, last_letter, str = \
                                common.common_exception_1(new_list, convertTuple(str_ending))
                            if ending in sourceModule.half_of_ending_for_general_possessiveness and new_list[
                                index - 1] in sourceModule.posessiveness_general:
                                new_list, index, ending, ending_list = common.common_exception_2(index, new_list,
                                                                                                 convertTuple(str_ending),
                                                                                                 ending_list, str)
                                continue
                        elif symbol == 'xp':
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))

                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue

                    elif symbol in sourceModule.for_poss and check_priority_of_endings.check_pl(self.__symbols_list):

                        self.__wrong_priority = True
                        break
                    elif symbol in sourceModule.for_poss:
                        if symbol in sourceModule.faces:
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                            common.faces(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list, self.__symbols)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue


                    elif symbol in sourceModule.negative and check_priority_of_endings.check_pl(self.__symbols_list):
                        new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                            common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                                       self.__symbols_list,
                                                       self.__symbols, ending_priority)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                    else:
                        self.__wrong_priority = True
                        break
                else:

                    new_list, index, last_letter, str = \
                            common.common_exception_1(new_list, convertTuple(str_ending))

                    if len(ending) == 2 and last_letter in sourceModule.special_vowel:

                        if not self.__symbols:
                            new_list, index, ending, ending_list, index2 = common.common_exception_3 \
                                (index, new_list, convertTuple(str_ending), ending_list, str)
                            if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                priority = 2
                                is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                    ending_priority, priority)
                                if is_correct_priority:
                                    new_list[index] = str[1:]
                                    str = str.replace(str[1:], '')
                                    new_list, new_word, self.__symbols, self.__symbols_list = common.common_exception_4(new_list, symbol, last_letter, str, self.__symbols, self.__symbols_list)
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
                                    self.__wrong_priority = True
                                    break
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in Possessiveness.posessiveness_2st_sg_politely or key in Possessiveness.posessiveness_1st_pl or key \
                                        in Possessiveness.posessiveness_2st_pl:
                                    priority = 2
                                    ending_priority = 4
                                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                        ending_priority, priority)
                                    is_px3sp = False
                                    if is_correct_priority:
                                        index, new_list, last_letter, ending, self.__symbols, ending_list = \
                                            common.common_exception_5(index, new_list, last_letter,
                                                                      convertTuple(str_ending),
                                                                      self.__symbols, ending_list, str)
                                    else:
                                        self.__wrong_priority = True
                                        break
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list, ending_list = common.common_exception_6(index, new_list,
                                                                                  convertTuple(str_ending),
                                                                                  ending_list, str)
                                if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    priority = 2
                                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                        ending_priority, priority)
                                    if is_correct_priority:
                                        new_list, ending_list = common.common_exception_4(index, new_list,
                                                                                          convertTuple(str_ending),
                                                                                          ending_list, str)
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
                                        self.__wrong_priority = True
                                        break

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
                            new_list, ending_list = common.common_exception_8(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)

                        except:
                            new_list, ending_list = common.common_exception_9(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)
                        str = listToString(new_list[index])
                        str = (str, )
                        symbol, priority = find_endings(str)
                        if symbol:
                            is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                ending_priority, priority)
                            if is_correct_priority:
                                new_list, new_word = common.common_exception_10(self, new_list,
                                                                                symbol, convertTuple(str))
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
                                self.__wrong_priority = True
                                break
                        else:
                            continue


# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'v':
                print('verb block')
                str_ending = (str_ending,)
                symbol, priority = find_endings(str_ending)
                if symbol:
                    priority = check_priority_of_endings.check_tag_for_verb(symbol, priority)
                    print('priority:{}'.format(priority))
                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(ending_priority,
                                                                                                    priority)
                    if is_correct_priority:
                        if symbol in sourceModule.faces:
                            self.__is_like_a_noun = True
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                                common.faces(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list,
                                             self.__symbols)

                        elif symbol in sourceModule.gerunds:
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol in sourceModule.chakchyl:
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol in sourceModule.atoochtuk:
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol in sourceModule.case:
                            self.__is_like_a_noun = True
                            if convertTuple(str_ending) in sourceModule.verb_pres:
                                print(33)
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol in sourceModule.possessiveness:
                            self.__is_like_a_noun = True
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                                common.possessiveness(index, new_list, symbol, convertTuple(str_ending),
                                                      self.__symbols_list,
                                                      self.__symbols)
                        elif symbol == sourceModule.plural:
                            strip_ending = convertTuple(str_ending)[1:]
                            strip_ending = (strip_ending,)
                            letter = convertTuple(str_ending)[0]
                            symbol, priority = find_endings(strip_ending)
                            if symbol:
                                is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                    ending_priority,
                                    priority)
                                if is_correct_priority:
                                    if self.find_root_from_the_end(new_word[:-2]):
                                        new_list, new_word = block_of_verb.special_future_tense(self, convertTuple(strip_ending), index,
                                                                                              new_list, symbol, letter)
                                        print(new_word)
                                else:
                                    self.__wrong_priority = True
                                    break

                            else:
                                self.__is_like_a_noun = True
                                new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                                common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                                           self.__symbols_list,
                                                           self.__symbols, ending_priority)
                            # new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        elif symbol == sourceModule.ques or symbol == sourceModule.agent_noun or symbol == sourceModule.negative:
                            print(12)


                            new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                                common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                                           self.__symbols_list,
                                                           self.__symbols, ending_priority)
                            print(new_word)
                        elif symbol == 'opt' and new_list[1] in sourceModule.posessiveness_general:
                            # for posessiveness_general (ныкы) итд
                            ending_priority = 5
                            new_list, index, last_letter, str = \
                                common.common_exception_1(new_list, convertTuple(str_ending))
                            if ending in sourceModule.half_of_ending_for_general_possessiveness and new_list[
                                index - 1] in sourceModule.posessiveness_general:
                                new_list, index, ending, ending_list = common.common_exception_2(index, new_list,
                                                                                                 convertTuple(
                                                                                                     str_ending),
                                                                                                 ending_list, str)
                                continue
                        elif symbol == 'xp':
                            self.__is_like_a_noun = True
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))

                        else:
                            new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue

                    elif symbol in sourceModule.for_poss and check_priority_of_endings.check_pl(self.__symbols_list):

                        self.__wrong_priority = True
                        break
                    elif symbol in sourceModule.for_poss:
                        if symbol in sourceModule.faces:
                            self.__is_like_a_noun = True
                            new_list, new_word, self.__symbols_list, self.__symbols = \
                                common.faces(index, new_list, symbol, convertTuple(str_ending), self.__symbols_list,
                                             self.__symbols)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue


                    elif symbol in sourceModule.negative and check_priority_of_endings.check_pl(self.__symbols_list):
                        self.__is_like_a_noun = True
                        new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                            common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                                       self.__symbols_list,
                                                       self.__symbols, ending_priority)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            continue
                    else:
                        self.__wrong_priority = True
                        break
                else:

                    strip_ending = convertTuple(str_ending)[1:]
                    strip_ending = (strip_ending,)
                    symbol, priority = find_endings(strip_ending)
                    if symbol:
                    #if strip_ending in sourceModule.ending_of_gerund or strip_ending in sourceModule.ending_of_gerund_pres:

                        #if (symbol := Verb.get_gerund(strip_ending)) != 'none':
                            #priority = 2
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                ending_priority, priority)
                        if is_correct_priority:
                            print('strip block')
                            print(symbol)
                            if symbol in sourceModule.inf1_2:
                                is_loc, ending, self.__symbols, self.__symbols_list = block_of_verb.is_ending_a_loc(self.__symbols, self.__symbols_list)
                                if is_loc:
                                    print('uuda')
                                    print(self.__symbols)
                                    new_list, new_word = block_of_verb.special_pres(self,
                                                                                      convertTuple(str_ending),
                                                                                    index, new_list, ending)
                                    print(new_word)
                                    if self.find_root_from_the_end(new_word):
                                        break
                                    else:
                                        new_list.reverse()
                                        continue
                                else:
                                    new_list, new_word = block_of_verb.special_gerund(self, convertTuple(str_ending),
                                                                                      symbol, index, new_list)


                            else:
                                print('yp, ysh, uu')
                                new_list, new_word = block_of_verb.special_gerund(self, convertTuple(str_ending), symbol, index, new_list)
                            print(new_word)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                continue
                        else:
                            self.__wrong_priority = True
                            break
                    else:
                        if convertTuple(str_ending) in sourceModule.for_pst_evid:
                            print(22)
                            print(new_list)
                            is_pst_evid, new_list, new_word = block_of_verb.is_ending_a_pst_evid(
                                self, new_list, index, convertTuple(str_ending))
                            if is_pst_evid:
                                print('yptyr')
                                print(new_word)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    new_list.reverse()
                                    continue
                        else:
                            new_list, new_word = block_of_verb.special_gerund(self, convertTuple(str_ending),
                                                                              symbol, index, new_list)
                    if convertTuple(str_ending)[-1] == 'п' and self.find_root_from_the_end(
                            self.__word_without_punctuation.lower()[:-1]):
                        priority = 2
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                            ending_priority, priority)
                        if is_correct_priority:
                            new_list, new_word = block_of_verb.special_chakchyl_1(self, ending, index, new_list)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                continue
                        else:
                            self.__wrong_priority = True
                            break


                    new_list, index, last_letter, str = \
                        common.common_exception_1(new_list, convertTuple(str_ending))

                    if len(ending) == 2 and last_letter in sourceModule.special_vowel:

                        if not self.__symbols:
                            new_list, index, ending, ending_list, index2 = common.common_exception_3 \
                                (index, new_list, convertTuple(str_ending), ending_list, str)
                            if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                priority = 4
                                is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                    ending_priority, priority)
                                if is_correct_priority:
                                    new_list[index] = str[1:]
                                    str = str.replace(str[1:], '')
                                    new_list, new_word, self.__symbols, self.__symbols_list = common.common_exception_4(
                                        new_list, symbol, last_letter, str, self.__symbols, self.__symbols_list)
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
                                    self.__wrong_priority = True
                                    break
                        else:
                            is_px3sp = True
                            for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                                if key in Possessiveness.posessiveness_2st_sg_politely or key in Possessiveness.posessiveness_1st_pl or key \
                                        in Possessiveness.posessiveness_2st_pl:
                                    priority = 4
                                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                        ending_priority, priority)
                                    is_px3sp = False
                                    if is_correct_priority:
                                        index, new_list, last_letter, ending, self.__symbols, ending_list = \
                                            common.common_exception_5(index, new_list, last_letter,
                                                                      convertTuple(str_ending),
                                                                      self.__symbols, ending_list, str)
                                    else:
                                        self.__wrong_priority = True
                                        break
                                else:
                                    continue
                            # px3sp with other endings
                            if is_px3sp:
                                new_list, ending_list = common.common_exception_6(index, new_list,
                                                                                  convertTuple(str_ending),
                                                                                  ending_list, str)
                                if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                                    priority = 4
                                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                        ending_priority, priority)
                                    if is_correct_priority:
                                        new_list, ending_list = common.common_exception_4(index, new_list,
                                                                                          convertTuple(str_ending),
                                                                                          ending_list, str)
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
                                        self.__wrong_priority = True
                                        break

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
                            new_list, ending_list = common.common_exception_8(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)

                        except:
                            new_list, ending_list = common.common_exception_9(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)
                        str = listToString(new_list[index])
                        str = (str,)
                        symbol, priority = find_endings(str)
                        if symbol:
                            is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                                ending_priority, priority)
                            if is_correct_priority:
                                new_list, new_word = common.common_exception_10(self, new_list,
                                                                                symbol, convertTuple(str))
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
                                self.__wrong_priority = True
                                break
                        else:
                            continue

# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == 'num':
                if (symbol := Numeral.get_info_numeral_ending(str_ending)) != 'none':
                    new_list, new_word = block_of_numeral.numeral(self, index, symbol, ending, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := Cases.get_info_cases(ending)) != 'none':
                    new_list, new_word = block_of_numeral.cases(self, index, symbol, ending, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := Faces.get_info_faces(ending)) != 'none':
                    new_list, new_word, self.__symbols_list, self.__symbols = \
                        common.faces(index, new_list, symbol, str_ending, self.__symbols_list, self.__symbols)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := Others.get_info_plural_for_num(ending)) != 'none':
                    new_list, new_word = block_of_numeral.plural(self, index, symbol, ending, new_list)
                    if self.find_root_from_the_end(new_word):

                        break
                    else:
                        continue
                elif (symbol := Others.get_info_other(ending)) != 'none':
                    new_list, new_word = block_of_numeral.numeral(self, index, symbol, ending, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
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
                elif ending in sourceModule.half_of_ending_for_ordinal_numeral:
                    new_list, first_letter, ending_list, str = block_of_numeral.ordinal_numeral_1(ending, new_list, ending_list)
                    if (symbol := Numeral.get_info_numeral_ending(str)) != 'none':
                        new_list, new_word = block_of_numeral.ordinal_numeral_2(self, index, symbol, str, new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_word = new_word + first_letter
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                continue
                elif ending in sourceModule.half_of_ending_for_not_sure_numeral:
                    new_list, ending_list, str = block_of_numeral.not_sure_numeral_1(ending, new_list, ending_list)
                    if (symbol := Numeral.get_info_numeral_ending(str)) != 'none':
                        new_list, new_word = block_of_numeral.not_sure_numeral_2(self, index, symbol, str,
                                                                                        new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
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
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adj":
                if (symbol := Adjectives_2.get_info_adj_ending(ending)) != 'none':
                    new_list, new_word = block_of_adjective.adj(self, index, ending, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        continue
                elif (symbol := Cases.get_info_cases(ending)) != 'none':
                    self.set_symbols_list = common.substantive(self.set_symbols_list)
                    new_list, new_word = block_of_adjective.common_adj(self, index, symbol, ending, new_list)
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
                    self.set_symbols_list = common.substantive(self.set_symbols_list)
                    new_list, new_word = block_of_adjective.common_adj(self, index, symbol, ending, new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := Possessiveness.get_info_possessive(ending)) != 'none':
                    self.set_symbols_list = common.substantive(self.set_symbols_list)
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
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
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
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------
            elif self.part_of_speech == "adv":
                if (symbol := Adverb.get_info_adv_ending(ending)) != 'none':
                    new_list, new_word = common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
                elif (symbol := Cases.get_info_cases(ending)) != 'none':
                    new_list, new_word = common.common(self, index, new_list, symbol, ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue
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
        self.__result_text, self.__all_info, self.__symbols_list = get_all_info.get_info(self, self.__symbols_list, self.__symbols,
                                                           self.__root, self.__part_of_speech,
                                                           self.__first_punctuation_mark,
                                                           self.__word_without_punctuation,
                                                           self.__last_punctuation_mark,
                                                            self.__wrong_priority)


        self.__symbols_list = [i for i in self.__symbols_list if i is not None]
        self.__symbols_list = list(dict.fromkeys(self.__symbols_list))



