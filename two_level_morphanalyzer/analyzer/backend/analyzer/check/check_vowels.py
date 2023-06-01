from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.analyzer.block.common import convertTuple

def get_last_vowel(lemma):
    lemma = convertTuple(lemma)
    vowel = ''
    for letter in lemma:
        if letter in sourceModule.vowels_kg:
            if letter == 'я':
                vowel = 'a'
            elif letter == 'ю':
                vowel = 'у'
            elif letter == 'ё':
                vowel = 'о'
            else:
                vowel = letter
    return vowel
def check_ending_vowels(last_vowel_of_lemma, affix):
    is_correct_type_of_vowel = False
    if last_vowel_of_lemma in sourceModule.narrow_vowels:
        for letter in affix:
            if letter in sourceModule.vowels_kg and letter in sourceModule.narrow_vowels:
                is_correct_type_of_vowel = True
            elif letter in sourceModule.vowels_kg and letter in sourceModule.wide_vowels:
                is_correct_type_of_vowel = False
    elif last_vowel_of_lemma in sourceModule.wide_vowels:
        for letter in affix:
            if letter in sourceModule.vowels_kg and letter in sourceModule.narrow_vowels:
                is_correct_type_of_vowel = False
            elif letter in sourceModule.vowels_kg and letter in sourceModule.wide_vowels:
                is_correct_type_of_vowel = True

    return is_correct_type_of_vowel

