from analyzer.backend.analyzer.exceptions import sourceModule

def get_info_pronoun_root(root):
    if root in personal_pronoun:
        return "pers"
    elif root in Demonstrative_pronoun:
        return "dem"
    elif root in Interrogative_pronoun:
        return "itg"
    elif root in Negative_pronoun:
        return "neg"
    elif root in Quantifier_pronoun:
        return "qnt"
    elif root in Indefinite_pronoun:
        return "ind"
    else:
        return "none"
def is_sg_or_pl(root):
    if root in pronoun_singular:
        if root in Personal_pronoun_first_person:
            return "p1sg"
        elif root in Personal_pronoun_second_person:
            return "p2sg"
        else:
            return "p3sg"
    elif root in pronoun_plural:
        if root in Personal_pronoun_first_person:
            return "p1pl"
        elif root in Personal_pronoun_second_person:
            return "p2pl"
        else:
            return "p3pl"

    else:
        return "none"
def cases_pronoun_root(root):
    if root in sourceModule.prn_gen:
        return 'gen'
    elif root in sourceModule.prn_dat:
        return 'dat'
    elif root in sourceModule.prn_acc:
        return 'acc'
    elif root in sourceModule.prn_loc:
        return 'loc'
    elif root in sourceModule.prn_abl:
        return 'abl'

all_pronoun ={
    'мен','сен','сиз','ал','биз','силер','сиздер','алар',
    'бу','бул','ушу','ушул','ошо','ошол','тиги','тигил','тетиги','тетигил', 'тээтетиги','тээтетигил',
    'ким','эмне','не','кандай','кайсы','кай','канча','нече','кайдан','качан', 'кайда','кана','кайсыл',
    'эч ким','эч нерсе','эчтеме','эч кандай','эч качан','эч кайда','эч кайдан','эч бир',
    'бүт','бүтүн','бүткүл','баары','бардык','ар ким','ар нерсе','ар бир', 'ар кайсы','ар кандай','өз',
    'алда ким','алда эмне','алда не','алда кандай','алда качан','алда канча',
                      'алда нече','алда кайда','алда кайдан','кимдир бирөө','кандайдыр бир','качандыр бир',
                      'эмнегедир','негедир','бир нерсе','бир неме','бирөө','бир деме','бир демке',
                      'бирдеме','неме','кайсы бир','кай бир','кээ бир','бири','кайсы бирөө'

}
personal_pronoun = {'мен','сен','сиз','ал','биз','силер','сиздер','алар',
        'менин','сенин','анын',
    'мага','сага','ага', 'мени','сени','аны', 'анда', 'андан'
                     }
pronoun_singular = {'мен','сен','сиз','ал', 'менин','сенин','анын',
    'мага','сага','ага', 'мени','сени','аны', 'анда', 'андан'
}
pronoun_plural = {'биз','силер','сиздер','алар'
}
Personal_pronoun_first_person ={'мен','биз', 'менин', 'мага', 'мени'
}
Personal_pronoun_second_person = {'сен','сиз','силер','сиздер', 'сенин', 'сага', 'сени'
}
Personal_pronoun_third_person = {'ал','алар', 'анын', 'ага', 'аны', 'анда', 'андан'
}

Demonstrative_pronoun = {'бу','бул','ушу','ушул','ошо','ошол','тиги','тигил','тетиги','тетигил',
                         'тээтетиги','тээтетигил', 'муну'
}
Interrogative_pronoun = {'ким','эмне','не','кандай','кайсы','кай','канча','нече','кайдан','качан',
                         'кайда','кана','кайсыл','кантип'

}
Negative_pronoun = {'эч ким','эч нерсе','эчтеме','эч кандай','эч качан','эч кайда','эч кайдан','эч бир'

}
Quantifier_pronoun = {'бүт','бүтүн','бүткүл','баары','бардык','ар ким','ар нерсе','ар бир',
                      'ар кайсы','ар кандай','өз','өзү'

}
Indefinite_pronoun = {'алда ким','алда эмне','алда не','алда кандай','алда качан','алда канча',
                      'алда нече','алда кайда','алда кайдан','кимдир бирөө','кандайдыр бир','качандыр бир',
                      'эмнегедир','негедир','бир нерсе','бир неме','бирөө','бир деме','бир демке',
                      'бирдеме','неме','кайсы бир','кай бир','кээ бир','бири','кайсы бирөө'

}

