from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.work_with_db.find_lemma import find_only_lemma
from analyzer.backend.work_with_db.find_lemma import find_lemma_for_verb
from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness


def find_root_from_the_end(self, new_word):
    new_word = (new_word,)
    is_found, self.__root = find_only_lemma(new_word)
    if is_found:
        is_found = find_lemma_for_verb(new_word)
        if is_found:
            return True
        else:
            return False
def verb_ending_from_verb(self, index, new_list, symbol, ending):
    new_list.reverse()
    new_word = listToString(new_list)
    new_list.reverse()
    self.set_root(new_word)
    self.set_part_of_speech(symbol)
    self.set_symbol('from_v_to_v', ending)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def noun_ending_from_verb(self, index, new_list, symbol, ending):
    new_list.reverse()
    new_word = listToString(new_list)
    new_list.reverse()
    self.set_root(new_word)
    self.set_part_of_speech(symbol)
    self.set_symbol('from_v_to_n', ending)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def special_gerund(self, ending, symbol, index, new_list):
    letter = ending[0]
    self.set_symbol(symbol, ending[1:])
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word

def special_pres(self, ending, index, new_list, key):
    letter = ending[0]
    self.set_symbol('pres', ending[1:]+key)
    self.set_symbols_list('pres')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word

def special_pst_evid(self, ending, index, new_list, key):
    letter = ending[0]
    self.set_symbol('pst_evid', ending[1:]+key)
    self.set_symbols_list('pst_evid')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word


def is_ending_a_loc(symbols, symbol_list):
    for key, tag in symbols.items():
        if key in sourceModule.verb_pres:
            del symbols[key]
            symbol_list.remove(tag)
            return True, key, symbols, symbol_list
    return False, '', symbols, symbol_list


def is_ending_a_pst_evid(self, new_list, index, last_ending, new_word):
    ending = new_list[1]
    if len(ending) == 3:
        if ending[1:] in sourceModule.for_pst_evid2:
            #yptyr
            new_list.pop(index)
            new_list.pop(index)
            new_list[0] = new_list[0]+ending[0]
            new_list.reverse()
            self.set_symbol('pst_evid', str(ending[1:]+last_ending))
            self.set_symbols_list('pst_evid')
            new_word = listToString(new_list)
            return True, new_list, new_word
        elif ending[:-1] in sourceModule.negative_ending_verb and ending[2] in sourceModule.for_pst_evid2:
            #yptyr with negative ending
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            self.set_symbol('pst_evid', str(ending[2] + last_ending))
            self.set_symbols_list('pst_evid')
            self.set_symbol('neg', str(ending[:-1]))
            self.set_symbols_list('neg')
            new_word = listToString(new_list)
            return True, new_list, new_word
        elif ending[2] in sourceModule.for_pst_evid2 and find_root_from_the_end(self, str(new_word[:-4])):
            #ptyr for vowel end verb
            new_list.pop(index)
            new_list[0] = ending[:-1]
            new_list.reverse()
            self.set_symbol('pst_evid', str(ending[2]+last_ending))
            self.set_symbols_list('pst_evid')
            new_word = listToString(new_list)
            return True, new_list, new_word
    return False, new_list, 'new_word'

def special_future_tense(self, ending, index, new_list, symbol, letter):
    self.set_symbol(symbol, str(ending))
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word
def special_chakchyl_1(self, ending, index, new_list):
    letters = ending[:-1]
    self.set_symbol('advv_acc', 'ып')
    self.set_symbols_list('advv_acc')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letters
    return new_list, new_word


def special_chakchyl_2(self, ending, symbol, index, new_list):
    letter = ending[0]
    self.set_symbol(symbol, ending[1:])
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word


def special_voice(self, ending, symbol, index, new_list):
    letter = ending[0]
    self.set_symbol(symbol, ending[1:])
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word


def fut_indf(self, ending, new_list):
    self.set_symbol('fut_indf', ending[-1])
    self.set_symbols_list('fut_indf')
    new_list[0] = ending[:-1]
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def fut_indf_neg(self, ending, new_list, index):
    self.set_symbol('fut_indf', ending[-1])
    self.set_symbols_list('fut_indf')
    self.set_symbol('neg', ending[:-1])
    self.set_symbols_list('neg')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word

def imp_pl(self, ending, new_list, index, new_word):
    next_ending = new_list[1]
    if next_ending in sourceModule.imp_pl_1 and new_list[2] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-6])):
        self.set_symbol('imp_pl', next_ending+ending)
        self.set_symbols_list('imp_pl')
        self.set_symbol('neg', new_list[2])
        self.set_symbols_list('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    elif next_ending in sourceModule.imp_pl_1:
        self.set_symbol('imp_pl', next_ending+ending)
        self.set_symbols_list('imp_pl')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def faces_for_verb(self, index, new_list, symbol, ending, symbols_list, symbols, new_word):
    print(new_word)
    print(new_list)
    if symbol == sourceModule.two_sgf:
        next_ending = new_list[1]
        if next_ending[-1] + ending in sourceModule.two_sgf_ending and find_root_from_the_end(self, str(new_word[:-4])):
            symbols[next_ending[-1] + ending] = 'imp_sgf'
            symbols_list.append('imp_sgf')
            new_list[1] = next_ending[0]
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
        else:
            symbols[ending] = 'imp_sgf'
            symbols_list.append('imp_sgf')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key in list(symbols.keys()):
        if ending in Faces.face_2st_sg_politely and key in Others.plural:  # сыздар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = '2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('2pl')
        elif ending in Others.negative and key in symbols:  # сыз
            symbols[ending] = 'neg'
            symbols_list.append('neg')

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols

def pl(self, ending, new_list, index, symbol):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_word, new_list

def imp_plf(self, index, new_list, ending, new_word, symbols, symbols_list):
    next_next_ending = new_list[1]
    ending_pl = ''
    for key, value in symbols.items():
        if value == 'pl':
            ending_pl = key
    if next_next_ending[-1] + ending in sourceModule.two_sgf_ending and \
            find_root_from_the_end(self, str(new_word[:-4])):
        #print('ynyzdar')
        symbols[next_next_ending[-1] + ending + ending_pl] = 'imp_plf'
        symbols_list.append('imp_plf')
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list[1] = next_next_ending[0]
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_word, new_list, symbols, symbols_list
    elif ending in sourceModule.imp_sgf and find_root_from_the_end(self, str(new_word[:-3])):
        #print('nyzdar')
        symbols[ending + ending_pl] = 'imp_plf'
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        print(new_word)
        return new_word, new_list, symbols, symbols_list
    elif ending in sourceModule.imp_sgf and new_list[1] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-5])):
        #print('banyzdar')
        symbols[ending + ending_pl] = 'imp_plf'
        symbols_list.append('imp_plf')
        symbols[new_list[1]] = 'neg'
        symbols_list.append('neg')
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_word, new_list, symbols, symbols_list