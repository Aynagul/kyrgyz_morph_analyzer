different_letter = {'я':'йа',
                    'ю':'йу',
                    'ё':'йо'}
def replace_letter(word):
    for letter in word:
        if letter in different_letter:
            word = word.replace(letter, str(different_letter.get(letter)))
    return word

posessiveness_general = {
    'ны', 'ни', 'ну', 'нү',
    'ды', 'ди', 'ду', 'дү',
    'ты', 'ти', 'ту', 'тү'
}
half_of_ending_for_general_possessiveness = ['кы', 'ки', 'ку', 'кү']
ending_of_gerund = ['уу','үү','оо','өө']
ending_of_gerund_pres = ['аш','ыш','иш','уш', 'үш','өш','ош']
ending_of_chakchyl = ['ып','ип','уп','үп','ап']
v_voice_all_ending = {
    'ын', 'ан', 'ун', 'үн', 'ың',   #эгин жүгүнөт
    'ыл', 'ол', 'өл', 'ул', 'үл',
    'ыш', 'иш',     #кылышты
    'аш', 'еш', 'уш', 'үш', #иштештик
    'ыр', 'ир', 'ур', 'үр',
    'ил'
}
case = ['gen','dat','acc','loc','abl']
voice = ['ref','coop','pass','caus']
mood = ['ind_pres','ind_past','ind_fut','cnd','niet','tilek']
non_finite_verb_forms = ['ger','gna_perf','ger_impf','gpr_perf','gpr_fut_neg','gpr_impf', 'gpr_pres', 'gpr_past', 'ger_pres',
                         'ger_pres']
face = ['p1sg','p1pl','p2sg','p2pl']
num_symbols = ['ord', 'top','coll','chamalama']
consonants_kg = {
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
}
special_vowel = {
    'и', 'ы', 'у', 'ү'
}
vowels_kg = {
    'а', 'о', 'ө', 'э', 'и', 'ы', 'у', 'ү', 'аа', 'оо', 'өө', 'ээ', 'уу', 'үү', 'я', 'ю', 'ё', 'е'
}
all_punctuation_marks = ['.',',','?','!','"',';',':','{','}','`']
sentence_end_p_m = ['. ','! ','? ']

half_of_ending_for_ordinal_numeral = ['чы', 'чи' , 'чу' , 'чү']
half_of_ending_for_not_sure_numeral = ['гон', 'гөн', 'ген', 'ган']

special_pronoun = ['менин','сенин','анын', 'мага','сага','ага', 'мени',
                   'сени','аны', 'анда', 'андан', 'муну', 'мунун', 'буга', 'мында', 'мындан']
prn_gen = {'менин','сенин','анын', 'мунун'}
prn_dat = {'мага','сага','ага', 'буга'}
prn_acc = {'мени','сени','аны', 'муну'}
prn_loc = {'анда', 'мында'}
prn_abl = {'андан', 'мындан'}