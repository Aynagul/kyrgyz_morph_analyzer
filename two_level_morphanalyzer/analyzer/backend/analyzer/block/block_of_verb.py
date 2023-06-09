from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.work_with_db.find_lemma import find_only_lemma
from analyzer.backend.work_with_db.find_lemma import is_lemma_in_db
from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness
from analyzer.backend.analyzer.check import check_priority_of_endings

def common_exception_for_verb(index, new_list, symbol, ending, symbols_list, symbols, priority):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    priority = priority
    for key in list(symbols.keys()):
        if ending in Faces.face_2st_sg_politely and key in Others.plural:  # сыздар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)

            symbols[ending + key] = 'p2plf'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('p2plf')

            priority = 5
        elif ending in Others.negative and key in Others.question:  #  бы
            symbols_list.remove(symbols[ending])
            symbols.pop(ending)

            symbols[ending] = 'p2sgf'
            symbols_list.append('p2sgf')

            priority = 5
        '''elif ending in Others.negative:  # сыз
            symbols[ending] = 'neg'
            symbols_list.append('neg')
            priority = 5'''


    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols, priority

def find_root_from_the_end(self, new_word):
    new_word = (new_word,)
    is_found, self.__root = find_only_lemma(new_word)
    if is_found:
        is_found = is_lemma_in_db(new_word)
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
    if symbol == 'ger_pres':
        for key, value in symbols.items():
            if value == 'imp':
                ending_jus_sg = key
                print('yshsyn')
                symbols_list.append('p3pl')
                symbols[ending[1:] + ending_jus_sg] = 'imp'
                #symbols_list.append('jus_pl')
                del symbols[ending_jus_sg]
                #symbols_list.remove('jus_sg')
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

def special_pres(self, ending, index, new_list, key, new_word):
    if ending[0] in sourceModule.neg_pre1 and find_root_from_the_end(self, str(new_word[:-3])):
        print('poodo')
        new_list.pop(index)
        new_list.reverse()
        self.set_symbol('pres', ending[1:] + key)
        self.set_symbols_list('pres')
        self.set_symbol('neg', ending[0] + 'а')
        self.set_symbols_list('neg')
        new_word = listToString(new_list)
        return new_list, new_word
    else:
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
    self.set_symbol('past_evid', ending[1:]+key)
    self.set_symbols_list('past_evid')
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
            self.set_symbol('past_evid', str(ending[1:]+last_ending))
            self.set_symbols_list('past_evid')
            new_word = listToString(new_list)
            return True, new_list, new_word
        elif ending[:-1] in sourceModule.negative_ending_verb and ending[2] in sourceModule.for_pst_evid2:
            #yptyr with negative ending
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            self.set_symbol('past_evid', str(ending[2] + last_ending))
            self.set_symbols_list('past_evid')
            self.set_symbol('neg', str(ending[:-1]))
            self.set_symbols_list('neg')
            new_word = listToString(new_list)
            return True, new_list, new_word
        elif ending[2] in sourceModule.for_pst_evid2 and find_root_from_the_end(self, str(new_word[:-4])):
            #ptyr for vowel end verb
            new_list.pop(index)
            new_list[0] = ending[:-1]
            new_list.reverse()
            self.set_symbol('past_evid', str(ending[2]+last_ending))
            self.set_symbols_list('past_evid')
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
    self.set_symbol('gna_perf', 'ып')
    self.set_symbols_list('gna_perf')
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


def fut_aor(self, ending, new_list):
    self.set_symbol('fut_aor', ending[-1])
    self.set_symbols_list('fut_aor')
    new_list[0] = ending[:-1]
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def fut_indf_neg(self, ending, new_list, index):
    self.set_symbol('fut_aor', ending[-1])
    self.set_symbols_list('fut_aor')
    self.set_symbol('neg', ending[:-1])
    self.set_symbols_list('neg')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word

def imp_p2pl(self, ending, new_list, index, new_word):
    next_ending = new_list[1]
    if next_ending in sourceModule.imp_pl_1 and new_list[2] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-6])):
        self.set_symbols_list('p2pl')
        self.set_symbol('imp', next_ending+ending)
        self.set_symbols_list('imp')
        self.set_symbol('neg', new_list[2])
        self.set_symbols_list('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    elif next_ending in sourceModule.imp_pl_1:
        self.set_symbols_list('p2pl')
        self.set_symbol('imp', next_ending+ending)
        self.set_symbols_list('imp')
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

        if ending in sourceModule.imp_p2sgf and find_root_from_the_end(self, str(new_word[:-3])):
            print('чуркаңыз')
            symbols_list.append('p2sgf')
            symbols[ending] = 'imp'
            symbols_list.append('imp')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
        elif next_ending[-1] + ending in sourceModule.two_sgf_ending and find_root_from_the_end(self, str(new_word[:-4])):

            symbols_list.append('p2sgf')
            symbols[next_ending[-1] + ending] = 'imp'
            symbols_list.append('imp')
            new_list[1] = next_ending[0]
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
        else:
            for key in list(symbols.keys()):

                if ending in Faces.face_2st_sg_politely and key in Others.plural:  # сыздар
                    symbols_list.remove('pl')

                    symbols[ending + key] = 'p2plf'
                    del symbols[key]
                    symbols_list.append('p2plf')
                    new_list.pop(index)
                    new_list.reverse()
                    new_word = listToString(new_list)
                    return new_list, new_word, symbols_list, symbols

            symbols[ending] = 'p2plf'
            symbols_list.append('p2plf')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
    symbols[ending] = symbol
    symbols_list.append(symbol)



    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols

def pl(self, ending, new_list, index, symbol, new_word):

    if ending[1:] in sourceModule.fut_aor and find_root_from_the_end(self, str(new_word[:-2])):
        print('ar')
        new_list[index] = ending[0]
        new_list.reverse()
        self.set_symbol('fut_aor', ending[1:])
        self.set_symbols_list('fut_aor')
        new_word = listToString(new_list)
        print(new_word)
        return new_word, new_list
    else:
        self.set_symbol(symbol, ending)
        self.set_symbols_list(symbol)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
    return new_word, new_list

def imp_p2plf(self, index, new_list, ending, new_word, symbols, symbols_list):
    next_next_ending = new_list[1]
    ending_pl = ''
    for key, value in symbols.items():
        if value == 'pl':
            ending_pl = key
    if next_next_ending[-1] + ending in sourceModule.two_sgf_ending and \
            find_root_from_the_end(self, str(new_word[:-4])):
        #print('ynyzdar')
        symbols_list.append('p2plf')
        symbols[next_next_ending[-1] + ending + ending_pl] = 'imp'
        symbols_list.append('imp')
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list[1] = next_next_ending[0]
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_word, new_list, symbols, symbols_list
    elif ending in sourceModule.imp_p2sgf and find_root_from_the_end(self, str(new_word[:-3])):
        #print('nyzdar')
        symbols_list.append('p2plf')
        symbols[ending + ending_pl] = 'imp'
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        print(new_word)
        return new_word, new_list, symbols, symbols_list
    elif ending in sourceModule.imp_p2sgf and new_list[1] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-5])):
        #print('banyzdar')
        symbols_list.append('p2plf')
        symbols[ending + ending_pl] = 'imp'
        symbols_list.append('imp')
        symbols[new_list[1]] = 'neg'
        symbols_list.append('neg')
        del symbols[ending_pl]
        symbols_list.remove('pl')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_word, new_list, symbols, symbols_list


def ger_pres(self, ending, new_list, index, new_word, symbols, symbols_list):

    for key, value in symbols.items():
        if value == 'imp':
            ending_jus_sg = key
            if ending[-1] in sourceModule.ger_pres and find_root_from_the_end(self, str(new_word[:-1])):
                #print('shsyn')
                symbols[ending[-1] + ending_jus_sg] = 'imp'
                #symbols_list.append('jus_pl')
                del symbols[ending_jus_sg]
                #symbols_list.remove('jus_sg')
                new_list[index] = ending[:-1]
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list
            elif ending[-1] in sourceModule.ger_pres and ending[:-1] in sourceModule.negative_ending_verb and \
                    find_root_from_the_end(self, str(new_word[:-3])):
                #print('bashsyn')
                symbols[ending[-1] + ending_jus_sg] = 'imp'
                #symbols_list.append('jus_pl')
                symbols[ending[:-1]] = 'neg'
                symbols_list.append('neg')
                del symbols[ending_jus_sg]
                #symbols_list.remove('jus_sg')
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list

    if ending[-1] in sourceModule.ger_pres and find_root_from_the_end(self, str(new_word[:-1])):
        #sh
        symbols[ending[-1]] = 'ger_pres'
        symbols_list.append('ger_pres')
        new_list[index] = ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def is_fut_indf(list):
    for i in list:
        if i == 'fut_indf':
            return True
        else:
            continue
    return False



def fut_indf_1(self, ending, new_list, index, new_word, symbols, symbols_list):

    for key, value in symbols.items():
        if value == 'fut_indf':
            ending_hor_sg = key
            if ending[-1] in sourceModule.fut_indf_endings and find_root_from_the_end(self, str(new_word[:-1])):
                print('ayin')
                symbols_list.append('p1sg')
                symbols[ending[-1] + ending_hor_sg] = 'fut_indf'
                del symbols[ending_hor_sg]
                new_list[index] = ending[:-1]
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list


def fut_indf_2(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if next_ending[-1] + ending in sourceModule.hor_pl3 and find_root_from_the_end(self, str(new_word[:-3])):
        #print('алы')
        symbols_list.append('p1pl')
        symbols[next_ending[-1] + ending] = 'fut_indf'
        symbols_list.append('fut_indf')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[-1] + ending in sourceModule.hor_pl3 and next_ending[:-1] in sourceModule.negative_ending_verb and \
            find_root_from_the_end(self, str(new_word[:-5])):
        #print('байлы')
        symbols_list.append('p1pl')
        symbols[next_ending[-1] + ending] = 'fut_indf'
        symbols_list.append('fut_indf')
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
        symbols_list.append('p1pl')
        symbols[next_ending[-1] + ending] = 'fut_indf'
        symbols_list.append('fut_indf')
        symbols[next_ending[:-1]] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[-1] + ending in sourceModule.hor_pl4 and find_root_from_the_end(self, str(new_word[:-4])):
        #print('алык')
        symbols_list.append('p1pl')
        symbols[next_ending[-1] + ending] = 'fut_indf'
        symbols_list.append('fut_indf')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def fut_indf_3(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    for key, value in symbols.items():
        if value == 'prec_1':
            ending_prec_1 = key
            if ending + ending_prec_1 in sourceModule.deside2 and find_root_from_the_end(self, str(new_word[:-3])):
                #print('макчы')
                symbols[ending + ending_prec_1] = 'fut_indf'
                symbols_list.append('fut_indf')
                del symbols[ending_prec_1]
                symbols_list.remove('prec_1')
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list
            elif ending + ending_prec_1 in sourceModule.deside2 and next_ending in sourceModule.negative_ending_verb and \
                    find_root_from_the_end(self, str(new_word[:-5])):
                #print('памакчы')
                symbols[ending + ending_prec_1] = 'fut_indf'
                symbols_list.append('fut_indf')
                del symbols[ending_prec_1]
                symbols_list.remove('prec_1')
                symbols[next_ending] = 'neg'
                symbols_list.append('neg')
                new_list.pop(index)
                new_list.pop(index)
                new_list.reverse()
                new_word = listToString(new_list)
                return new_list, new_word, symbols, symbols_list



    if check_priority_of_endings.check_change_ending(symbols_list):
        symbols[ending] = 'ger_fut'
        symbols_list.append('ger_fut')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    else:
        symbols[ending] = 'fut_indf'
        symbols_list.append('fut_indf')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def fut_opt(self, ending, new_list, index, new_word):
    if ending in sourceModule.inf_5_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        self.set_symbol('p1sg', ending[-1])
        self.set_symbols_list('p1sg')
        self.set_symbol('fut_opt', ending[:-1])
        self.set_symbols_list('fut_opt')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    elif ending in sourceModule.inf_5_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        self.set_symbol('p2sg', ending[-1])
        self.set_symbols_list('p2sg')
        self.set_symbol('fut_opt', ending[:-1])
        self.set_symbols_list('fut_opt')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def past_def(self, ending, new_list, index):
    self.set_symbol('past_def', ending)
    self.set_symbols_list('past_def')
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word

def fut_indf_neg_with_neg(self, ending, new_list, index, new_word, symbols, tag):
    for key, value in symbols.items():
        if value == 'fut_indf_neg':
            return True, new_list, new_word
    self.set_symbol(tag, ending)
    self.set_symbols_list(tag)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return False, new_list, new_word


def possessiveness_for_verb(self, index, new_list, symbol, ending, symbols_list, symbols, new_word):
    next_ending = new_list[1]
    for key, value in symbols.items():
        if ending in Possessiveness.posessiveness_for_poses_2st_pl_politely and key in Others.plural:  # ыңыздар итд

            symbols[ending + key] = 'px2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('px2pl')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols, 4

        elif ending in Possessiveness.posessiveness_for_face_p2pl and key in Possessiveness.posessiveness_2st_pl:  # сыңар

            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('p2pl')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols, 4
    if next_ending[-1] + ending in sourceModule.two_sgf_ending and find_root_from_the_end(self, str(new_word[:-4])):
        symbols[next_ending[-1] + ending] = 'imp_sgf'
        symbols_list.append('imp_sgf')
        new_list.pop(index)
        new_list[index] = next_ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols_list, symbols, 2
    elif symbol == 'px2sgf':
        symbols[ending] = 'imp_sgf'
        symbols_list.append('imp_sgf')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols_list, symbols, 2
    symbols[ending] = symbol
    symbols_list.append(symbol)


    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)

    return new_list, new_word, symbols_list, symbols, 4


def gna_purp(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    next_next_ending = new_list[2]
    if next_ending in sourceModule.advv_int2 and find_root_from_the_end(self, str(new_word[:-4])):

        #print('ганы')

        symbols[next_ending + ending] = 'gna_purp'
        symbols_list.append('gna_purp')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending in sourceModule.advv_int2 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-6])):

        #print('баганы')

        symbols[next_ending + ending] = 'gna_purp'
        symbols_list.append('gna_purp')
        symbols[next_next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def gna_cnd(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    next_next_ending = new_list[2]
    if next_ending + ending in sourceModule.advv_suc1 and find_root_from_the_end(self, str(new_word[:-4])):

        #print('гыча')
        symbols[next_ending + ending] = 'gna_irre'
        symbols_list.append('gna_irre')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending + ending in sourceModule.advv_suc2 and find_root_from_the_end(self, str(new_word[:-5])):

        #print('ганча')

        symbols[next_ending + ending] = 'gna_irre'
        symbols_list.append('gna_irre')

        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_next_ending + next_ending + ending in sourceModule.gna_cnd and find_root_from_the_end(self, str(new_word[:-7])):

        #print('майынча')
        symbols[next_next_ending + next_ending + ending] = 'gna_cnd'
        symbols_list.append('gna_cnd')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list



def advv_neg2(self, ending, new_list, index, new_word, symbols, symbols_list, symbol):
    next_ending = new_list[1]
    if next_ending + ending in sourceModule.advv_neg2 and find_root_from_the_end(self, str(new_word[:-5])):
        #print('майын')

        symbols[next_ending + ending] = 'gna_cnd'
        symbols_list.append('gna_cnd')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    symbols[ending] = symbol
    symbols_list.append(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols, symbols_list



def gpr_1(self, ending, new_list, index, new_word, symbols, symbols_list, symbol):
    next_ending = new_list[1]
    if next_ending[1:] + ending in sourceModule.gpr_1 and find_root_from_the_end(self, str(new_word[:-4])):
        #print('оочу')
        symbols[next_ending[1:] + ending] = 'gpr'
        symbols_list.append('gpr')
        new_list.pop(index)
        new_list[index] = next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_ending[1:] + ending in sourceModule.gpr_1 and next_ending[0] in sourceModule.neg_pre1 and find_root_from_the_end(self, str(new_word[:-5])):
        #print('боочу')
        symbols[next_ending[1:] + ending] = 'gpr'
        symbols_list.append('gpr')
        symbols[next_ending[0] + 'а'] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    symbols[ending] = symbol
    symbols_list.append(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols, symbols_list



def gpr_impf(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    next_next_ending = new_list[2]
    if ((next_ending + ending in sourceModule.pcp_fut_def1 and find_root_from_the_end(self, str(new_word[:-5]))) or
        (next_ending + ending in sourceModule.pcp_fut_def2 and find_root_from_the_end(self, str(new_word[:-5]))) or
        (next_ending + ending in sourceModule.pcp_fut_def3 and find_root_from_the_end(self, str(new_word[:-6])))):
        #print('гыдай,чудай,гандай')
        symbols[next_ending + ending] = 'gpr_impf'
        symbols_list.append('gpr_impf')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif ((next_ending + ending in sourceModule.pcp_fut_def1 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-7]))) or
        (next_ending + ending in sourceModule.pcp_fut_def2 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-7]))) or
        (next_ending + ending in sourceModule.pcp_fut_def3 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-8])))):
        #print('пагыдай,почудай,багандай')

        symbols[next_ending + ending] = 'gpr_impf'
        symbols_list.append('gpr_impf')
        symbols[next_next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def gpr_pres(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    next_next_ending = new_list[2]
    if next_ending + ending in sourceModule.gpr_pres2 and find_root_from_the_end(self, str(new_word[:-6])):
        #print('максан')
        symbols[next_ending + ending] = 'gpr_pres'
        symbols_list.append('gpr_pres')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending + ending in sourceModule.gpr_pres2 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-8])):
        #print('бамаксан')
        symbols[next_ending + ending] = 'gpr_pres'
        symbols_list.append('gpr_pres')
        symbols[next_next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def pst_def_face(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if ending[-1] == sourceModule.shortcut_face_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        #print('дим')

        symbols[ending[-1]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[-1] == sourceModule.shortcut_face_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('диң')

        symbols[ending[-1]] = 'p2sg'
        symbols_list.append('p2sg')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[-1] == sourceModule.shortcut_face_1pl and find_root_from_the_end(self, str(new_word[:-3])):
        # print('дик')
        symbols[ending[-1]] = 'p1pl'
        symbols_list.append('p1pl')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[-1] == sourceModule.shortcut_face_1sg and next_ending in sourceModule.negative_ending_verb \
            and find_root_from_the_end(self, str(new_word[:-5])):
        #print('бедим')

        symbols[ending[-1]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[-1] == sourceModule.shortcut_face_2sg and next_ending in sourceModule.negative_ending_verb \
            and find_root_from_the_end(self, str(new_word[:-5])):
        #print('бедиң')
        symbols[ending[-1]] = 'p2sg'
        symbols_list.append('p2sg')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[-1] == sourceModule.shortcut_face_1pl and next_ending in sourceModule.negative_ending_verb \
            and find_root_from_the_end(self, str(new_word[:-5])):
        #print('бедик')

        symbols[ending[-1]] = 'p1pl'
        symbols_list.append('p1pl')
        symbols[ending[:-1]] = 'past_def'
        symbols_list.append('past_def')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def shortcut_ending_with_1_sg_3sg(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if ending[1:] in sourceModule.shortcut_ending_with_1_sg and find_root_from_the_end(self, str(new_word[:-2])):
        print('fut_def 1_sg')

        symbols[ending[-1]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[1]] = 'fut_def'
        symbols_list.append('fut_def')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.shortcut_ending_with_3_sg and find_root_from_the_end(self, str(new_word[:-2])):
        print('fut_def 3_sg')

        symbols[ending[-1]] = 'p3sg'
        symbols_list.append('p3sg')
        symbols[ending[1]] = 'fut_def'
        symbols_list.append('fut_def')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.cond_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        #print('сам')

        symbols[ending[2]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'cnd'
        symbols_list.append('cnd')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.cond_1sg and next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-5])):
        #print('басам')

        symbols[ending[2]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'cnd'
        symbols_list.append('cnd')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def fut_def_faces(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if find_root_from_the_end(self, str(new_word[:-1])):
        #print('fut_def other faces')
        symbols[ending[-1]] = 'fut_def'
        symbols_list.append('fut_def')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def pres_with_faces(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if next_ending[1:] in sourceModule.ending_of_gerund and find_root_from_the_end(self, str(new_word[:-4])):
        symbols[next_ending[1:] + ending] = 'pres'
        symbols_list.append('pres')
        new_list.pop(index)
        new_list[index] = next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending[0] in sourceModule.neg_pre1 and next_ending[1:] in sourceModule.ending_of_gerund and find_root_from_the_end(self, str(new_word[:-5])):
        symbols[next_ending[1:] + ending] = 'pres'
        symbols_list.append('pres')
        symbols[next_ending[0] + 'а'] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def pst_iter_faces(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if ending in sourceModule.pst_iter_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        #print('чум')

        symbols[ending[-1]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.pst_iter_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('чуң')

        symbols[ending[-1]] = 'p2sg'
        symbols_list.append('p2sg')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.pst_iter_1pl and find_root_from_the_end(self, str(new_word[:-3])):
        # print('чук')

        symbols[ending[-1]] = 'p1pl'
        symbols_list.append('p1pl')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.pst_iter_1sg and next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-5])):
        # print('бачум')

        symbols[ending[-1]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.pst_iter_2sg and next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-5])):
        # print('бачуң')

        symbols[ending[-1]] = 'p2sg'
        symbols_list.append('p2sg')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.pst_iter_1pl and next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-5])):
        # print('бачук')
        symbols[ending[-1]] = 'p1pl'
        symbols_list.append('p1pl')
        symbols[ending[:-1]] = 'past_iter'
        symbols_list.append('past_iter')
        symbols[next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def fut_def_special(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if find_root_from_the_end(self, str(new_word[:-2])):
        #print('чуркайм')

        symbols[ending[3]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[2]] = 'fut_def'
        symbols_list.append('fut_def')
        new_list[index] = ending[:-2]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[:-2] in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-4])):
        # print('чуркабайм')

        symbols[ending[3]] = 'p1sg'
        symbols_list.append('p1sg')
        symbols[ending[2]] = 'fut_def'
        symbols_list.append('fut_def')
        symbols[ending[:2]] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def fut_def_special_negative(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if find_root_from_the_end(self, str(new_word[:-3])):
        #print('бай, ...')
        symbols[ending[2]] = 'fut_def'
        symbols_list.append('fut_def')
        symbols[ending[:-1]] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def cond_faces(self, ending, new_list, index, new_word, symbols, symbols_list):

    if ending in sourceModule.cond_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('саң')

        symbols[ending[2]] = 'p2sg'
        symbols_list.append('p2sg')
        symbols[ending[:-1]] = 'cnd'
        symbols_list.append('cnd')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending in sourceModule.cond_1pl and find_root_from_the_end(self, str(new_word[:-3])):
        # print('сак')

        symbols[ending[2]] = 'p1pl'
        symbols_list.append('p1pl')
        symbols[ending[:-1]] = 'cnd'
        symbols_list.append('cnd')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def inf_1_inf_2_with_shortcut_faces(self, ending, new_list, index, new_word, symbols, symbols_list):
    next_ending = new_list[1]
    if ending[1:] in sourceModule.inf_1_with_shortcut_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        #print('оом')

        symbols[ending[3]] = 'px1sg'
        symbols_list.append('px1sg')
        symbols[ending[1:-1]] = 'ger'
        symbols_list.append('ger')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.inf_2_with_shortcut_1sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('уум')

        symbols[ending[3]] = 'px1sg'
        symbols_list.append('px1sg')
        symbols[ending[1:-1]] = 'ger'
        symbols_list.append('ger')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.inf_1_with_shortcut_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('ооң')

        symbols[ending[3]] = 'px2sg'
        symbols_list.append('px2sg')
        symbols[ending[1:-1]] = 'ger'
        symbols_list.append('ger')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.inf_2_with_shortcut_2sg and find_root_from_the_end(self, str(new_word[:-3])):
        # print('ууң')

        symbols[ending[3]] = 'px2sg'
        symbols_list.append('px2sg')
        symbols[ending[1:-1]] = 'ger'
        symbols_list.append('ger')
        new_list[index] = ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def different_tags_with_poss_1_2(self, ending, new_list, index, new_word, symbols, symbols_list, tag, strip_ending):
    next_ending = new_list[1]
    next_next_ending = new_list[2]
    symbols[strip_ending] = tag
    symbols_list.append(tag)


    if next_ending[-1] + ending[0] in sourceModule.ger_pres and find_root_from_the_end(self, str(new_word[:-4])):
        #print('ger_pres with poss')
        symbols[next_ending[-1] + ending[0]] = 'ger_pres'
        symbols_list.append('ger_pres')
        new_list.pop(index)
        new_list[index] = next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_ending + ending[0] in sourceModule.gpr_2 and find_root_from_the_end(self, str(new_word[:-5])):
        # print('gpr with poss')
        symbols[next_ending + ending[0]] = 'gpr'
        symbols_list.append('gpr')

        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_ending + ending[0] in sourceModule.gpr_2 and next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-7])):
        # print('gpr with neg, poss')
        symbols[next_ending + ending[0]] = 'gpr'
        symbols_list.append('gpr')
        symbols[next_next_ending] = 'neg'
        symbols_list.append('neg')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending + ending[0] in sourceModule.plural_ending and next_next_ending[1:] in sourceModule.inf_1_ending and find_root_from_the_end(self, str(new_word[:-7])):

        # print('ger with pl,poss')
        symbols[next_ending + ending[0]] = 'pl'
        symbols_list.append('pl')
        symbols[next_next_ending[1:]] = 'ger'
        symbols_list.append('ger')
        new_list.pop(index)
        new_list.pop(index)
        new_list[index] = next_next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif next_ending + ending[0] in sourceModule.plural_ending and next_next_ending[1:] in sourceModule.inf_2_ending and find_root_from_the_end(self, str(new_word[:-7])):

        # print('ger with pl,poss')
        symbols[next_ending + ending[0]] = 'pl'
        symbols_list.append('pl')
        symbols[next_next_ending[1:]] = 'ger'
        symbols_list.append('ger')
        new_list.pop(index)
        new_list.pop(index)
        new_list[index] = next_next_ending[0]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    elif next_ending + ending[0] in sourceModule.plural_ending and next_next_ending in sourceModule.gpr_2 and find_root_from_the_end(self, str(new_word[:-8])):
        # print('gpr with pl,poss')
        symbols[next_ending + ending[0]] = 'pl'
        symbols_list.append('pl')
        symbols[next_next_ending] = 'gpr'
        symbols_list.append('gpr')
        new_list.pop(index)
        new_list.pop(index)
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

    if len(new_list) > 4:

        next_next_next_ending = new_list[3]
        if next_ending + ending[0] in sourceModule.plural_ending and next_next_next_ending[1:] + next_next_ending in sourceModule.pcp_pr_1 \
                and find_root_from_the_end(self, str(new_word[:-9])):

            print('gpr with pl, poss')
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            symbols[next_next_next_ending[1:] + next_next_ending] = 'gpr'
            symbols_list.append('gpr')
            new_list.pop(index)
            new_list.pop(index)
            new_list.pop(index)
            new_list[index] = next_next_next_ending[0]
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list

        elif next_ending + ending[0] in sourceModule.plural_ending and next_next_ending in sourceModule.gpr_2 and \
                next_next_next_ending in sourceModule.negative_ending_verb and find_root_from_the_end(self, str(new_word[:-10])):
            # print('gpr with neg,pl,poss')
            symbols[next_ending + ending[0]] = 'pl'
            symbols_list.append('pl')
            symbols[next_next_ending] = 'gpr'
            symbols_list.append('gpr')
            symbols[next_next_next_ending] = 'neg'
            symbols_list.append('neg')
            new_list.pop(index)
            new_list.pop(index)
            new_list.pop(index)
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols, symbols_list

def advv_acc_latest_letter(self, ending, new_list, index, new_word, symbols, symbols_list):

    if find_root_from_the_end(self, str(new_word[:-1])):

        print('gna_perf short ending')
        symbols[ending[2]] = 'gna_perf'
        symbols_list.append('gna_perf')
        new_list[index] = ending[:-1]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    elif ending[1:] in sourceModule.ending_of_chakchyl and find_root_from_the_end(self, str(new_word[:-2])):

        print('gna_perf')
        symbols[ending[1:]] = 'gna_perf'
        symbols_list.append('gna_perf')
        new_list[index] = ending[:-2]
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list

def pcp_indf(self, ending, new_list, index, new_word, symbols, symbols_list):
    print(symbols_list)
    if check_priority_of_endings.check_change_ending(symbols_list):

        print('gpr')
        symbols[ending] = 'gpr'
        symbols_list.append('gpr')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    else:

        print('past_indf')
        symbols[ending] = 'past_indf'
        symbols_list.append('past_indf')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def gpr_aor_neg(self, ending, new_list, index, new_word, symbols, symbols_list):
    if check_priority_of_endings.check_change_ending(symbols_list):
        print('gpr_aor_neg')
        symbols[ending] = 'gpr_aor_neg'
        symbols_list.append('gpr_aor_neg')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    else:
        print('fut_indf_neg')
        symbols[ending] = 'fut_indf_neg'
        symbols_list.append('fut_indf_neg')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list


def inf_5_with_other_tags(self, ending, new_list, index, new_word, symbols, symbols_list):

    if check_priority_of_endings.check_change_ending(symbols_list):

        symbols[ending] = 'fut_opt'
        symbols_list.append('fut_opt')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list
    else:


        symbols[ending] = 'fut_aor'
        symbols_list.append('fut_aor')
        new_list.pop(index)
        new_list.reverse()
        new_word = listToString(new_list)
        return new_list, new_word, symbols, symbols_list