from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness

def strip_affix_from_word(word, lemma):

    return word[len(lemma):]

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def common(self, index, new_list, symbol, ending):
    self.set_symbol(symbol, str(ending))
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word


def get_poss_ending(symbols):
    for key, value in symbols.items():
        if value == 'px2sgf':
            return True, str(key)
        elif value == 'px2pl':
            return True, str(key)
        elif value == 'px1pl':
            return True, str(key)
        elif value == 'px2plf':
            return True, str(key)
        elif value == 'p2plf':
            return True, str(key)
    return False, ''
def substantive(symbols_list):#затташып кеткен
    symbols_list.append('subst')
    return symbols_list


def faces(index, new_list, symbol, ending, symbols_list, symbols):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key in list(symbols.keys()):
        if ending in Faces.face_2st_sg_politely and key in Others.plural:  # сыздар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('p2pl')

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols


def possessiveness(index, new_list, symbol, ending, symbols_list, symbols):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key, value in symbols.items():
        if ending in Possessiveness.posessiveness_for_poses_2st_pl_politely and key in Others.plural:  # ыңыздар итд
            symbols_list.remove(value)
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'px2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list('px2pl')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
        elif ending in Possessiveness.posessiveness_for_face_p2pl and key in Possessiveness.posessiveness_2st_pl:  # сыңар

            symbols_list.remove(value)
            del symbols[key]
            del symbols[ending]
            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbol)
            symbols_list.append('p2pl')
            new_list.pop(index)
            new_list.reverse()
            new_word = listToString(new_list)
            return new_list, new_word, symbols_list, symbols
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols


def common_exception_1(new_list, ending):
    new_list.reverse()
    index = new_list.index(ending)
    str = listToString(ending)
    last_letter = str[-1]
    return new_list, index, last_letter, str


def common_exception_2(index, new_list, ending, ending_list, str):
    print(12)
    new_list[index - 1] = new_list[index - 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    new_list.pop(index)
    new_list.reverse()
    return new_list, index, ending, ending_list



def common_exception_11(index, new_list, symbol, ending, symbols_list, symbols, priority):

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
        elif ending in Possessiveness.posessiveness_2st_sg_politely and key in Others.plural:  # ңиздер
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'px2plf'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('px2plf')
            priority = 2
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