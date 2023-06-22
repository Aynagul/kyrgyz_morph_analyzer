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
    vowel_list = []
    for letter in affix:
        if letter in sourceModule.vowels_kg:
            vowel_list.append(letter)
    if not bool(vowel_list):
        is_correct_type_of_vowel = True
        return is_correct_type_of_vowel
    if last_vowel_of_lemma in sourceModule.narrow_vowels:
        for vowel in vowel_list:
            if vowel in sourceModule.narrow_vowels:
                is_correct_type_of_vowel = True
            elif vowel in sourceModule.wide_vowels:
                is_correct_type_of_vowel = False
                return is_correct_type_of_vowel
    elif last_vowel_of_lemma in sourceModule.wide_vowels:
        for vowel in vowel_list:
            if vowel in sourceModule.narrow_vowels:
                is_correct_type_of_vowel = False
                return is_correct_type_of_vowel
            elif vowel in sourceModule.wide_vowels:
                is_correct_type_of_vowel = True


    return is_correct_type_of_vowel

