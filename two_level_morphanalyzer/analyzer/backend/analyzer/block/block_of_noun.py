from analyzer.backend.analyzer.block.common import listToString, get_poss_ending
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

def short_poss_ending(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if find_root_from_the_end(self, str(new_word[:-1])):

        if ending[-1] == sourceModule.shortcut_face_1sg:
            print(11)
            symbols[ending[-1]] = 'px1sg'
            symbols_list.append('px1sg')
        elif ending[-1] == sourceModule.shortcut_face_2sg:
            symbols[ending[-1]] = 'px2sg'
            symbols_list.append('px2sg')


        new_list[0] = ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.poss_1sg_endings and find_root_from_the_end(self, str(new_word[:-2])):
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
    elif next_ending + ending[0] in sourceModule.plural_ending and ending[1:] in sourceModule.poss_1sg_endings and find_root_from_the_end(self, str(new_word[:-5])):
        print('px1sg with pl')
        symbols[ending[1:]] = 'px1sg'
        symbols_list.append('px1sg')
        symbols[next_ending + ending[0]] = 'pl'
        symbols_list.append('pl')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending + ending[0] in sourceModule.plural_ending and ending[1:] in sourceModule.poss_2sg_endings and find_root_from_the_end(self, str(new_word[:-5])):
        print('px2sg with pl')
        symbols[ending[1:]] = 'px2sg'
        symbols_list.append('px2sg')
        symbols[next_ending + ending[0]] = 'pl'
        symbols_list.append('pl')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list






def poss(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    is_poss, preivous_ending = get_poss_ending(symbols)
    if is_poss:
        if preivous_ending in sourceModule.px2sgf_endings and find_root_from_the_end(self, str(new_word[:-1])):
            print(new_word)
            print('px2sgf')
            symbols[ending[-1] + preivous_ending] = 'px2sgf'
            del symbols[preivous_ending]
            new_list[index] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif preivous_ending in sourceModule.px1pl_endings and find_root_from_the_end(self, str(new_word[:-1])):
            print('px1pl')
            symbols[ending[-1] + preivous_ending] = 'px1pl'
            del symbols[preivous_ending]
            new_list[index] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif preivous_ending in sourceModule.px2pl_endings and find_root_from_the_end(self, str(new_word[:-1])):
            print('px2pl')
            symbols[ending[-1] + preivous_ending] = 'px2pl'
            del symbols[preivous_ending]
            new_list[index] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif preivous_ending in Possessiveness.posessiveness_2st_pl_politely and find_root_from_the_end(self, str(new_word[:-1])):
            print('px2plf')
            symbols[ending[-1] + preivous_ending] = 'px2plf'
            del symbols[preivous_ending]
            new_list[index] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif next_ending + ending[0] in sourceModule.plural_ending and ending[-1] + preivous_ending in \
                Possessiveness.posessiveness_2st_pl and find_root_from_the_end(self, str(new_word[:-4])):
            print('px2pl with pl')
            symbols[ending[-1] + preivous_ending] = 'px2pl'
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            del symbols[preivous_ending]
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif next_ending + ending[0] in sourceModule.plural_ending and ending[-1] + preivous_ending in \
                Possessiveness.posessiveness_2st_sg_politely and find_root_from_the_end(self, str(new_word[:-4])):
            print('px2sgf with pl')
            symbols[ending[-1] + preivous_ending] = 'px2sgf'
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            del symbols[preivous_ending]
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif next_ending + ending[0] in sourceModule.plural_ending and ending[-1] + preivous_ending in Possessiveness.posessiveness_1st_pl and find_root_from_the_end(self, str(new_word[:-4])):
            print('px1pl with pl')
            symbols[ending[-1] + preivous_ending] = 'px1pl'
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            del symbols[preivous_ending]
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list
        elif next_ending + ending[0] in sourceModule.plural_ending and ending[-1] + preivous_ending in Possessiveness.posessiveness_2st_pl_politely and find_root_from_the_end(self, str(new_word[:-4])):
            print('px2plf with pl')
            symbols[ending[-1] + preivous_ending] = 'px2plf'
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            del symbols[preivous_ending]
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list

    else:

        if ending[-1] in sourceModule.shortcut_poss_3sg_ending and find_root_from_the_end(self, str(new_word[:-1])):
            print(12)
            symbols[ending[-1]] = 'px3sg'
            symbols_list.append('px3sg')
            new_list[0] = ending[:-1]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list

