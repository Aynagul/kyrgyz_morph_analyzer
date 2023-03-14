from analyzer.backend.analyzer.block.common import listToString

def adj(self, index, ending, new_list):
    self.set_symbol('from_adj_to_adj', ending)
    new_list.pop(index)
    new_list_2 = list(new_list)
    new_list_2.reverse()
    new_word = listToString(new_list_2)
    return new_list, new_word


def common_adj(self, index, symbol, ending, new_list):
    self.set_symbol(symbol, ending)
    self.set_symbols_list(symbol)
    new_list.pop(index)
    new_list.reverse()
    new_word = listToString(new_list)
    return new_list, new_word

