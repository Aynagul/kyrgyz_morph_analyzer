from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.check import check_priority_of_endings
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.work_with_db.find_lemma import find_only_lemma

from analyzer.backend.work_with_db.find_lemma import is_lemma_in_db

def numeral(self, index, symbol, ending, new_list):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list_2 = list(new_list)
    new_list_2.reverse()
    new_word = listToString(new_list_2)
    return new_list, new_word


def cases(self, index, symbol, ending, new_list):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    self.set_symbols_list('subst')  # subst - затташып кеткен символ
    new_list.pop(index)
    new_list_2 = list(new_list)
    new_list_2.reverse()
    new_word = listToString(new_list_2)
    return new_list, new_word

def plural(self, index, symbol, ending, new_list):
    self.set_symbols_list('pl')
    self.set_symbols_list(symbol)
    self.set_symbol('pl', ending)
    new_list.pop(index)
    new_list_2 = list(new_list)
    new_list_2.reverse()
    new_word = listToString(new_list_2)
    return new_list, new_word

def ordinal_numeral_1(ending, new_list, ending_list):
    new_list.reverse()
    index = new_list.index(ending)
    str = listToString(new_list[index - 1])
    new_list[index] = str[1:] + new_list[index]
    str = str.replace(str[1:], '')
    new_list[index - 1] = str
    ending_list[index - 1] = str
    str = listToString(new_list[index])
    first_letter = str[0]
    return new_list, first_letter, ending_list, str


def ordinal_numeral_2(self, index, symbol, str, new_list):
    self.set_symbol(symbol, str)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word

def not_sure_numeral_1(ending, new_list, ending_list):
    new_list.reverse()
    index = new_list.index(ending)
    str = listToString(new_list[index - 1])
    new_list[index] = str + new_list[index]
    new_list[index - 1] = str
    ending_list[index - 1] = str
    str = listToString(new_list[index])
    return new_list, ending_list, str


def not_sure_numeral_2(self, index, symbol, str, new_list):
    self.set_symbol(symbol, str)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.pop(index - 1)
    new_word = listToString(new_list)
    return new_list, new_word


def if_is_digit(symbols_list, word_without_punctuation):
    root = word_without_punctuation
    symbols_list.append('num')
    symbols_list.append('card')
    part_of_speech = 'num'
    return root, symbols_list, part_of_speech


def find_root_from_the_end(self, new_word):
    new_word = (new_word,)
    is_found, self.__root = find_only_lemma(new_word)
    if is_found:

        is_found = is_lemma_in_db(new_word)

        if is_found:
            return True
        else:
            return False

def num_ord(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    print(new_list)
    if next_ending[-1] + ending in sourceModule.num_ord_short and find_root_from_the_end(self, str(new_word[:-3])):
        print('нчи')
        symbols[next_ending[-1] + ending] = 'num_ord'
        symbols_list.append('num_ord')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[1:] + ending in sourceModule.num_ord and find_root_from_the_end(self, str(new_word[:-4])):
        symbols[next_ending[1:] + ending] = 'num_ord'
        symbols_list.append('num_ord')
        new_list.pop(index)
        new_list[index] = next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def num_top(self, ending, new_list, index, new_word, symbols, symbols_list):
    if find_root_from_the_end(self, str(new_word[:-3])):
        symbols[ending] = 'num_top'
        symbols_list.append('num_top')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def num_appr3(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if next_ending + ending in sourceModule.num_appr3 and find_root_from_the_end(self, str(new_word[:-5])):
        symbols[next_ending + ending] = 'num_appr3'
        symbols_list.append('num_appr3')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
