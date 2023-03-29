from analyzer.backend.analyzer.check.check_symbols import delete_symbols

def get_info(symbols_list, symbols, root, part_of_speech, first_punctuation_mark,
             word_without_punctuation, last_punctuation_mark, wrong_priority):
    if wrong_priority:
        return 'Wrong priority of endings', 'Something goes wrong'
    if 'sg' in symbols_list and 'pl' in symbols_list:
        symbols_list.remove('sg')
    for symbol in symbols_list:
        if symbol == '':
            symbols_list.remove(symbol)
    symbols_list = list(dict.fromkeys(symbols_list))  # delete duplicates symbols
    for symbol in symbols_list:
        symbols_list = delete_symbols(symbols_list, symbol)
    symbols_list = [i for i in symbols_list if i]
    all_info = "Уңгу: " + str(root) + ".\n" + "Сөз түркүм: " + str(part_of_speech) + \
                      ".\n" + "Баардык символдор: " + str(list(dict.fromkeys(symbols_list))) + ".\n" + \
                      "Мүчөлөр: " + str(symbols) + '\n'
    symbols_text = ''
    ending_symbols = []
    for key, value in dict(reversed(list(symbols.items()))).items():
        symbols_text = symbols_text + str(key) + '<' + str(value) + '>'
        ending_symbols.append(str(value))
    for sym in list(dict.fromkeys(symbols_list)):
        if sym in ending_symbols:
            symbols_list.remove(sym)

    def_symbols_text = ''
    for sym in list(dict.fromkeys(symbols_list)):
        def_symbols_text = def_symbols_text + '<' + str(sym) + '>'
    result_text = str(first_punctuation_mark) + str(word_without_punctuation) + \
                         "/" + str(root) + def_symbols_text + symbols_text + str(last_punctuation_mark)
    return result_text, all_info