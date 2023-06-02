from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.work_with_db.find_lemma import find_only_lemma
from analyzer.backend.work_with_db.find_lemma import is_lemma_in_db
from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness
from analyzer.backend.analyzer.check import check_priority_of_endings

def adverb_ending_from_noun(self, index, new_list, symbol, ending):
    new_list.reverse()
    new_word = listToString(new_list)
    new_list.reverse()
    self.set_root(new_word)
    self.set_part_of_speech(symbol)
    self.set_symbol('from_n_to_adv', ending)
    self.set_symbols_list(symbol)

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def noun_ending_from_noun(self, index, new_list, symbol, ending):
    new_list.reverse()
    new_word = listToString(new_list)
    new_list.reverse()
    self.set_root(new_word)
    self.set_part_of_speech(symbol)
    self.set_symbol('from_n_to_n', ending)
    self.set_symbols_list(symbol)

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def noun_to_adj(self, index, new_list, symbol, ending, new_word):
    new_list.reverse()
    self.set_root(new_word)
    new_list.reverse()
    self.set_part_of_speech(symbol)
    self.set_symbol('from_n_to_adj', ending)
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

def short_poss_ending(self, ending, new_list):
    if ending[-1] == sourceModule.shortcut_face_1sg:
        self.set_symbol('px1sg', ending[-1])
        self.set_symbols_list('px1sg')
    elif ending[-1] == sourceModule.shortcut_face_2sg:
        self.set_symbol('px2sg', ending[-1])
        self.set_symbols_list('px2sg')
    elif ending[-1] == sourceModule.shortcut_poss_3sg_ending:
        self.set_symbol('px3sg', ending[-1])
        self.set_symbols_list('px3sg')
    new_list[0] = ending[:-1]
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def poss_1sg_2sg(self, ending, new_list, index, new_word, symbols, symbols_list):
    if ending[1:] in sourceModule.poss_1sg_endings and find_root_from_the_end(self, str(new_word[:-2])):
        print('px1sg')
        symbols[ending[1:]] = 'px1sg'
        symbols_list.append('px1sg')
        new_list[index] = ending[:-2]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.poss_2sg_endings and find_root_from_the_end(self, str(new_word[:-2])):
        print('px2sg')
        symbols[ending[1:]] = 'px2sg'
        symbols_list.append('px2sg')
        new_list[index] = ending[:-2]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def px2sgf(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    for key, value in symbols.items():
        if value == 'px2sgf':
            ending_px2sgf = key
            print('px2sgf')
            symbols[ending[-1] + ending_px2sgf] = 'px2sgf'
            symbols_list.append('px1sg')
            del symbols[ending_px2sgf]
            new_list[index] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list

