def situation_1(word):#Ex: word,
    last_punctuation_mark = word[-1] + ' '
    word_without_punctuation = word[:-1]
    return last_punctuation_mark, word_without_punctuation


def situation_2(word):#Ex: ,word
    first_punctuation_mark = word[0]
    word_without_punctuation = word[1:]
    return first_punctuation_mark, word_without_punctuation


def situation_3(word):#Ex: ,word,
    first_punctuation_mark = word[0]
    last_punctuation_mark = word[-1] + ' '
    word_without_punctuation = word[1:-1]
    return first_punctuation_mark, last_punctuation_mark, word_without_punctuation