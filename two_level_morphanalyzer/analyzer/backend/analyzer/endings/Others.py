def get_info_other(ending):
    if ending in negative:
        return "neg"
    elif ending in agent_noun:
        return "agnt"
    elif ending in question:
        return "ques"
    elif ending in plural:
        return "pl"
    else:
        return 'none'
def get_info_plural_for_num(ending):
    if ending in plural:
        return "subst"
    else:
        return 'none'
agent_noun = {
    'чы', 'чи', 'чу', 'чү'
}
question = {
    'би', 'бы', 'бу', 'бү',
    'пи', 'пы', 'пу', 'пү',
}
negative = {
    'ба', 'бе', 'бө', 'бо',
    'па', 'пе', 'пө', 'по',
    'сыз', 'сиз', 'сүз', 'суз',
}
plural ={
    'дар', 'дер', 'дор', 'дөр',
    'тар', 'тер', 'тор', 'төр',
    'лар', 'лер', 'лор', 'лөр',
}