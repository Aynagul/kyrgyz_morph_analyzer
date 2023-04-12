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


def special_gerund(self, ending, symbol, index, new_list, symbols, symbols_list):
    if symbol == 'inf_3':
        for key, value in symbols.items():
            if value == 'jus_sg':
                ending_jus_sg = key
                print('yshsyn')
                symbols[ending[1:] + ending_jus_sg] = 'jus_pl'
                symbols_list.append('jus_pl')
                del symbols[ending_jus_sg]
                symbols_list.remove('jus_sg')
                new_list[index] = ending[0]
                new_list.reverse()
                new_word = listToString(new_list)
                print(new_word)
                return new_list, new_word, symbols, symbols_list
    letter = ending[0]
    self.set_symbol(symbol, ending[1:])
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    new_word = new_word + letter
    return new_list, new_word, symbols, symbols_list

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


def inf_3(self, ending, new_list, index, new_word, symbols, symbols_list):

    for key, value in symbols.items():
        if value == 'jus_sg':
            ending_jus_sg = key
            if ending[-1] in sourceModule.inf_3 and find_root_from_the_end(self, str(new_word[:-1])):
                #print('shsyn')
                symbols[ending[-1] + ending_jus_sg] = 'jus_pl'
                symbols_list.append('jus_pl')
                del symbols[ending_jus_sg]
                symbols_list.remove('jus_sg')
                new_list[index] = ending[:-1]
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list
            elif ending[-1] in sourceModule.inf_3 and ending[:-1] in sourceModule.negative_ending_verb and \
                    find_root_from_the_end(self, str(new_word[:-3])):
                #print('bashsyn')
                symbols[ending[-1] + ending_jus_sg] = 'jus_pl'
                symbols_list.append('jus_pl')
                symbols[ending[:-1]] = 'neg'
                symbols_list.append('neg')
                del symbols[ending_jus_sg]
                symbols_list.remove('jus_sg')
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list

    if ending[-1] in sourceModule.inf_3 and find_root_from_the_end(self, str(new_word[:-1])):
        #sh
        symbols[ending[-1]] = 'inf_3'
        symbols_list.append('inf_3')
        new_list[index] = ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def is_hor_sg(list):
    for i in list:
        if i == 'hor_sg':
            return True
        else:
            continue
    return False
def hor_sg(self, ending, new_list, index, new_word, symbols, symbols_list):
    for key, value in symbols.items():
        if value == 'hor_sg':
            ending_hor_sg = key
            if ending[-1] in sourceModule.hor_sg and find_root_from_the_end(self, str(new_word[:-1])):
                print('ayin')
                symbols[ending[-1] + ending_hor_sg] = 'hor_sg'
                del symbols[ending_hor_sg]
                new_list[index] = ending[:-1]
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list


def hor_pl(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if next_ending[-1] + ending in sourceModule.hor_pl3 and find_root_from_the_end(self, str(new_word[:-3])):
        #print('алы')
        symbols[next_ending[-1] + ending] = 'hor_pl'
        symbols_list.append('hor_pl')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[-1] + ending in sourceModule.hor_pl3 and next_ending[:-1] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-5])):
        #print('байлы')
        symbols[next_ending[-1] + ending] = 'hor_pl'
        symbols_list.append('hor_pl')
        symbols[next_ending[:-1]] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[-1] + ending in sourceModule.hor_pl4 and next_ending[:-1] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-6])):
        #print('пайлык')
        symbols[next_ending[-1] + ending] = 'hor_pl'
        symbols_list.append('hor_pl')
        symbols[next_ending[:-1]] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[-1] + ending in sourceModule.hor_pl4 and find_root_from_the_end(self, str(new_word[:-4])):
        #print('алык')
        symbols[next_ending[-1] + ending] = 'hor_pl'
        symbols_list.append('hor_pl')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def deside(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    for key, value in symbols.items():
        if value == 'prec_1':
            ending_prec_1 = key
            if ending + ending_prec_1 in sourceModule.deside2 and find_root_from_the_end(self, str(new_word[:-3])):
                #print('макчы')
                symbols[ending + ending_prec_1] = 'deside'
                symbols_list.append('deside')
                del symbols[ending_prec_1]
                symbols_list.remove('prec_1')
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list
            elif ending + ending_prec_1 in sourceModule.deside2 and next_ending in sourceModule.negative_ending_verb and \
                    find_root_from_the_end(self, str(new_word[:-5])):
                #print('памак')
                symbols[ending + ending_prec_1] = 'deside'
                symbols_list.append('deside')
                del symbols[ending_prec_1]
                symbols_list.remove('prec_1')
                symbols[next_ending] = 'neg'
                symbols_list.append('neg')
                new_list.pop(index)
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list
    symbols[ending] = 'deside'
    symbols_list.append('deside')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols, symbols_list

def inf_5(self, ending, new_list, index, new_word):
    if ending in sourceModule.inf_5_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        self.set_symbol('1sg', ending[-1])
        self.set_symbols_list('1sg')
        self.set_symbol('inf_5', ending[:-1])
        self.set_symbols_list('inf_5')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    elif ending in sourceModule.inf_5_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        self.set_symbol('2sg', ending[-1])
        self.set_symbols_list('2sg')
        self.set_symbol('inf_5', ending[:-1])
        self.set_symbols_list('inf_5')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def pst_def(self, ending, new_list, index):
    self.set_symbol('pst_def', ending)
    self.set_symbols_list('pst_def')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word