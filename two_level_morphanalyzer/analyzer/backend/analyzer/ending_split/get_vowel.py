from analyzer.backend.analyzer.exceptions.sourceModule import different_letter

def replace_letter(word):
    for letter in word:
        if letter in different_letter:
            word = word.replace(letter, str(different_letter.get(letter)))
    return word

print(replace_letter(input()))

