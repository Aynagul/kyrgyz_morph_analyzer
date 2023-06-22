def situation_1(word):#Ex: word,
    return word[-1] + ' ', word[:-1], word[:-1].lower()


def situation_2(word):#Ex: ,word
    return word[0], word[1:], word[1:].lower()

def situation_3(word):#Ex: ,word,
    return word[0], word[-1] + ' ', word[1:-1], word[1:-1].lower()