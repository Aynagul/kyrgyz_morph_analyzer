def check_pronouns(self, symbol, word):
    root = ''
    if symbol == 'gen':
        if word == 'анын':
            self.set_symbol(symbol, 'нын')
            root = 'ал'
        elif word == 'менин':
            self.set_symbol(symbol, 'нин')
            root = 'мен'
        elif word == 'сенин':
            self.set_symbol(symbol, 'нин')
            root = 'сен'
        elif word == 'мунун':
            self.set_symbol(symbol, 'нун')
            root = 'бул'
    elif symbol == 'dat':
        if word == 'ага':
            self.set_symbol(symbol, 'га')
            root = 'ал'
        elif word == 'мага':
            self.set_symbol(symbol, 'га')
            root = 'мен'
        elif word == 'сага':
            self.set_symbol(symbol, 'га')
            root = 'сен'
        elif word == 'буга':
            self.set_symbol(symbol, 'га')
            root = 'бул'
    elif symbol == 'acc':
        if word == 'аны':
            self.set_symbol(symbol, 'ны')
            root = 'ал'
        elif word == 'мени':
            self.set_symbol(symbol, 'ни')
            root = 'мен'
        elif word == 'сени':
            self.set_symbol(symbol, 'ни')
            root = 'сен'
        elif word == 'муну':
            self.set_symbol(symbol, 'ну')
            root = 'бул'
    elif symbol == 'loc':
        if word == 'анда':
            self.set_symbol(symbol, 'да')
            root = 'ал'
        elif word == 'мында':
            self.set_symbol(symbol, 'да')
            root = 'бул'
    elif symbol == 'abl':
        if word == 'андан':
            self.set_symbol(symbol, 'дан')
            root = 'ал'
        elif word == 'мындан':
            self.set_symbol(symbol, 'дан')
            root = 'бул'
    return root