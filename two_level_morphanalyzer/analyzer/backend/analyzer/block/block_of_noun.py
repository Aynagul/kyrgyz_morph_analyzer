from analyzer.backend.analyzer.block.common import listToString

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


