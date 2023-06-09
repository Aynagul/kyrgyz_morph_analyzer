from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.check import check_priority_of_endings
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.work_with_db.find_lemma import find_only_lemma

from analyzer.backend.work_with_db.find_lemma import is_lemma_in_db


def adj(self, index, ending, new_list):
    self.set_symbol('from_adj_to_adj', ending)
    new_list.pop(index)
    new_list_2 = list(new_list)
    new_list_2.reverse()
    new_word = listToString(new_list_2)
    return new_list, new_word


def common_adj(self, index, symbol, ending, new_list):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word

def find_root_from_the_end(self, new_word):
    new_word = (new_word,)
    is_found, self.__root = find_only_lemma(new_word)
    if is_found:

        is_found = is_lemma_in_db(new_word)

        if is_found:
            return True
        else:
            return False

def comp(self, ending, new_list, index, new_word, symbols, symbols_list):

    next_ending = new_list[1]

    if find_root_from_the_end(self, str(new_word[:-4])):
        symbols[ending] = 'comp'
        symbols_list.append('comp')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_ending[-1] in sourceModule.comp_endings and find_root_from_the_end(self, str(new_word[:-5])):
        symbols[next_ending[-1]+ ending] = 'comp'
        symbols_list.append('comp')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

