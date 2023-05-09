from analyzer.backend.analyzer.exceptions import sourceModule
def add_char(word):
    t = ''
    for i in word:
        t += i
    return t
def ending_split(words):
    syllables_of_words_all = []
    if len(words) >= 1:
        for word in words:
            ls_word = list(word)
            ls_word_orig = list(word)
            syllables_of_words = []
            if ls_word_orig[0] in sourceModule.consonants_kg:
                while True:
                    if len(ls_word) == 4:
                        '''if ls_word[0] in analyzer.sourceModule.consonants_kg and ls_word[1] in analyzer.sourceModule.consonants_kg and ls_word[
                            2] in analyzer.sourceModule.vowels_kg and ls_word[3] in analyzer.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))'''
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[
                            2] in sourceModule.consonants_kg and (ls_word[3] == 'м' or ls_word[3]=='т'):
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[
                            2] in sourceModule.vowels_kg and ls_word[3] in sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                    elif len(ls_word) == 3:
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[2] in sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[2] in sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    elif len(ls_word) == 2:
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    if len(ls_word) == 0:
                        if len(ls_word_orig) <= 0:
                            break
                        else:
                            for i in range(len(syllables_of_words[-1])):
                                ls_word_orig.pop()
                            for i in ls_word_orig:
                                ls_word.append(i)
                    elif len(ls_word) != 0:
                        ls_word.remove(ls_word[0])
            elif ls_word_orig[0] in sourceModule.vowels_kg:
                first_letter = ''
                if len(ls_word_orig) >= 3:
                    if ls_word_orig[0] in sourceModule.vowels_kg and ls_word_orig[1] in sourceModule.consonants_kg and ls_word_orig[2] in sourceModule.vowels_kg:
                        first_letter = ls_word_orig[0]
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    elif ls_word_orig[0] in sourceModule.vowels_kg and ls_word_orig[1] in sourceModule.consonants_kg and ls_word_orig[2] in sourceModule.consonants_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]
                        ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    elif ls_word_orig[0] in sourceModule.vowels_kg and ls_word_orig[1] in sourceModule.vowels_kg and ls_word_orig[2] in sourceModule.consonants_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]
                        ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])
                    '''elif ls_word[0] in analyzer.sourceModule.vowels_kg and ls_word[1] in analyzer.sourceModule.consonants_kg and ls_word[
                            2] in analyzer.sourceModule.consonants_kg and ls_word[3] in analyzer.sourceModule.vowels_kg:
                        first_letter = ls_word_orig[0]+ls_word_orig[1]

ls_word.remove(ls_word[0])
                        ls_word.remove(ls_word[0])
                        ls_word_orig.remove(ls_word_orig[0])
                        ls_word_orig.remove(ls_word_orig[0])'''



                while True:
                    if len(ls_word) == 4:
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[
                            2] in sourceModule.consonants_kg and (ls_word[3] == 'м' or ls_word[3]=='т'):
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[
                            2] in sourceModule.vowels_kg and ls_word[3] in sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        '''elif ls_word[0] in analyzer.sourceModule.consonants_kg and ls_word[1] in analyzer.sourceModule.consonants_kg and ls_word[
                            2] in analyzer.sourceModule.vowels_kg and ls_word[3] in analyzer.sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))'''
                    elif len(ls_word) == 3:
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[2] in sourceModule.consonants_kg:
                            syllables_of_words.append(add_char(ls_word))
                        elif ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg and ls_word[2] in sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))

                    elif len(ls_word) == 2:
                        if ls_word[0] in sourceModule.consonants_kg and ls_word[1] in sourceModule.vowels_kg:
                            syllables_of_words.append(add_char(ls_word))
                    if len(ls_word) == 0:
                        if len(ls_word_orig) <= 0:
                            syllables_of_words.append(first_letter)
                            break
                        else:
                            for i in range(len(syllables_of_words[-1])):
                                ls_word_orig.pop()
                            for i in ls_word_orig:
                                ls_word.append(i)

                    elif len(ls_word) != 0:
                        ls_word.remove(ls_word[0])

            syllables_of_words.reverse()
            syllables_of_words_all.append(syllables_of_words)
    else:
        return False
    return syllables_of_words_all[0]