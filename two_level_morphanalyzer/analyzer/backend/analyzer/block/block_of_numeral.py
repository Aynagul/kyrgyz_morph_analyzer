from analyzer.backend.analyzer.block.common import listToString

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