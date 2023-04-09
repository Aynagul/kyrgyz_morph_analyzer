from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.exceptions import sourceModule

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


def is_ending_a_pst_evid(self, new_list, index, last_ending):
    ending = new_list[1]
    if len(ending) == 3:
        if ending[1:] in sourceModule.for_pst_evid2:
            new_list.pop(index)
            print(new_list)
            new_list.pop(index)
            print(new_list)
            new_list[0] = new_list[0]+ending[0]
            new_list.reverse()
            self.set_symbol('pst_evid', str(ending[1:]+last_ending))
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

