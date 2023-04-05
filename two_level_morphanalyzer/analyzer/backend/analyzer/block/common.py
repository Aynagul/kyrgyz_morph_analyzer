from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness
from analyzer.backend.analyzer.endings import Faces, Others, Possessiveness


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
        elif ending in Others.negative and key in symbols:  # сыз
            symbols[ending] = 'neg'
            symbols_list.append('neg')

    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols


def possessiveness(index, new_list, symbol, ending, symbols_list, symbols):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    for key in list(symbols.keys()):
        if ending in Possessiveness.posessiveness_for_poses_2st_pl_politely and key in Others.plural:  # ыңыздар итд
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'px2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list('px2pl')
        elif ending in Possessiveness.posessiveness_for_face_p2pl and key in Possessiveness.posessiveness_2st_pl:  # сыңар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = 'p2pl'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list('p2pl')
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
    new_list[index - 1] = new_list[index - 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    new_list.pop(index)
    new_list.reverse()
    return new_list, index, ending, ending_list


def common_exception_3(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, index, ending, ending_list, index2


def common_exception_4(new_list, symbol, last_letter, str, symbols, symbols_list):
    symbols[last_letter] = symbol
    symbols_list.append(symbol)
    index = new_list.index(last_letter)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word, symbols, symbols_list


def common_exception_5(index, new_list, last_letter, ending, symbols, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    new_ending = list(symbols)[-1]
    symbols[last_letter + new_ending] = symbols.pop(new_ending)
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    new_list.pop(index)
    #new_list.reverse()
    return index, new_list, last_letter, ending, symbols, ending_list


def common_exception_6(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str[0]
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, ending_list


def common_exception_7(self, symbol, new_list, last_letter, str):
    self.set_symbol(symbol, last_letter)
    self.set_symbols_list(symbol)
    index = new_list.index(str)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word


def common_exception_8(index, new_list, ending, ending_list, str):
    new_list[index + 1] = new_list[index + 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index + 1]
    ending_list.pop(index2)
    return new_list, ending_list


def common_exception_9(index, new_list, ending, ending_list, str):
    new_list[index - 1] = new_list[index - 1] + str
    index2 = ending_list.index(ending)
    ending_list[index2 + 1] = new_list[index - 1]
    return new_list, ending_list


def common_exception_10(self, new_list, symbol, str):
    self.set_symbol(symbol, str)
    self.set_symbols_list(symbol)
    index = new_list.index(str)
    new_list.pop(index)
    new_word = listToString(new_list)
    return new_list, new_word

def common_exception_11(index, new_list, symbol, ending, symbols_list, symbols, priority):
    symbols[ending] = symbol
    symbols_list.append(symbol)
    priority = priority
    for key in list(symbols.keys()):
        if ending in Faces.face_2st_sg_politely and key in Others.plural:  # сыздар
            symbols_list.remove(symbols[ending])
            symbols[ending + key] = symbols.pop(ending)
            symbols[ending + key] = '2plf'
            symbols_list.remove(symbols[key])
            symbols.pop(key)
            symbols_list.append('2plf')
            priority = 5
        elif ending in Others.negative and key in Others.question:  #  бы
            symbols_list.remove(symbols[ending])
            symbols.pop(ending)
            symbols[ending] = '2sgf'
            symbols_list.append('2sgf')
            priority = 5
        '''elif ending in Others.negative:  # сыз
            symbols[ending] = 'neg'
            symbols_list.append('neg')
            priority = 5'''


    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word, symbols_list, symbols, priority