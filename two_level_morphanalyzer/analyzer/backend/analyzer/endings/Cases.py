def get_info_cases(ending):
    if ending in case_genitive_simple or ending in case_genitive_hard:
        return "gen"    #илик жондомо
    elif ending in case_dative_simple or ending in case_dative_hard:
        return "dat"    #барыш
    elif ending in case_accusative_simple or ending in case_accusative_hard:
        return "acc"    #табыш
    elif ending in case_locative_simple:
        return "loc"    #жатыш
    elif ending in case_ablative_simple or ending in case_ablative_hard:
        return "abl"    #чыгыш
    else:
        return 'none'
case_genitive_simple = {
    'нын', 'дын', 'тын', 'нин', 'дин', 'тин', 'нүн', 'дүн', 'түн', 'нун', 'дун', 'тун'
}
case_dative_simple = {
    'га', 'ге', 'го', 'гө', 'ка', 'ке', 'ко', 'кө'
}
case_accusative_simple = {
    'ны', 'ды', 'ты', 'ни', 'ди', 'ти', 'нү', 'дү', 'тү', 'ну', 'ду', 'ту'
}
case_locative_simple = {
    'да', 'та', 'де', 'те', 'до', 'то', 'дө', 'тө'
}
case_ablative_simple = {
    'дан', 'тан', 'ден', 'тен', 'дон', 'тон', 'дөн', 'төн'
}
#hard means after possessive, num_collective, some pronoun,
case_genitive_hard = {
    'ын', 'ын', 'ын', 'ин', 'ин', 'ин', 'үн', 'үн', 'үн', 'ун', 'ун', 'ун'
}
case_dative_hard = {
    'а', 'е', 'о'
}

case_accusative_hard = {
    'ы', 'и', 'у', 'ү'
}
case_ablative_hard = {
    'ан', 'ан', 'ен', 'ен', 'он', 'он', 'өн', 'өн'
}
