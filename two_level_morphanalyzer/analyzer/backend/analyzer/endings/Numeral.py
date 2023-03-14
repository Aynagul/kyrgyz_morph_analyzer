def get_info_numeral_ending(ending):
    if ending in num_ending_ordinal:
        return "ord"
    elif ending in num_ending_fraction_and_top:
        return "top"
    elif ending in num_ending_collective:
        return "coll"
    elif ending in num_ending_not_sure:
        return "chamalama"
    else:
        return 'none'


num_ending_ordinal = {  # иреттик сан атооч
    'ынчы', 'инчи', 'үнчү', 'унчу', 'нчы', 'нчи'
}
num_ending_collective = {  # жамдама сан атооч
    'оо', 'өө'
}
num_ending_not_sure = {  # чамалама сан атооч
    'дай', 'дой', 'дей', 'дөй',
    'тай', 'той', 'тей', 'төй',
    'ча', 'чө', 'че', 'чо',
    'догон', 'дөгөн', 'деген', 'даган',
    'тогон', 'төгөн', 'теген', 'таган',
    'дук', 'дап', 'дүк', 'дөп', 'деп', 'дик', 'доп',
    'лөп', 'лап', 'леп', 'лоп',
    'тап', 'теп', 'топ', 'төп'
}
num_root_not_sure = {  # чамалама сан атооч
    'чамалуу', 'чакты', 'чамалаган', 'ашык', 'артык', 'ашуун', 'аша', 'көп', 'аз', 'жакын'
}
num_ending_fraction_and_top = {  # бөлчөк жана топ сан атоочтор
    'дан', 'тан', 'ден', 'тен', 'дон', 'тон', 'дөн', 'төн'
}
num_root_fraction = {
    'жарым', 'жарты', 'бүтүн', 'чейрек',
}
num_root = {"нөл", "бир", "эки", "үч", "төрт", "беш", "алты", "жети", "сегиз", "тогуз", "он",
            "жыйырма", "отуз", "кырк", "элүү", "алтымыш", "жетимиш", "сексен", "токсон", "жүз",
            "миң", "миллион", "миллиард"}
num_numeral = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
num_degree = {"10", "100", "1000", "1000000", "1000000000"}


def get_num(number):
    num = 0
    if number == "бир":
        num = 1
    elif number == "нөл":
        num = 0
    elif number == "он":
        num = 10
    elif number == "жүз":
        num = 100
    elif number == "миң":
        num = 1000
    elif number == "эки":
        num = 2
    elif number == "үч":
        num = 3
    elif number == "төрт":
        num = 4
    elif number == "беш":
        num = 5
    elif number == "алты":
        num = 6
    elif number == "жети":
        num = 7
    elif number == "сегиз":
        num = 8
    elif number == "тогуз":
        num = 9
    elif number == "жыйырма":
        num = 20
    elif number == "отуз":
        num = 30
    elif number == "кырк":
        num = 40
    elif number == "элүү":
        num = 50
    elif number == "алтымыш":
        num = 60
    elif number == "жетимиш":
        num = 70
    elif number == "сексен":
        num = 80
    elif number == "токсон":
        num = 90
    elif number == "миллион":
        num = 10 ** 6
    elif number == "миллиард":
        num = 10 ** 9
    return num


def get_degree(num):
    sum = 0
    num_degree_thousand = 0
    num_degree_million = 0
    num_degree_milliard = 0
    if True:
        for n in num:
            if str(n) in num_degree:
                if str(n) == "1000":
                    num_degree_thousand = sum * n
                    sum = 0
                elif str(n) == "1000000000":
                    num_degree_milliard = sum * n
                    sum = 0
                elif str(n) == "1000000":
                    num_degree_million = sum * n
                    sum = 0
                else:
                    sum = sum * n
            elif str(n) in num_numeral:
                sum = sum + n
            else:
                sum = sum + n
    return sum + num_degree_thousand + num_degree_million + num_degree_milliard


def get_info_numeral(numbers):
    total_number = 0
    all_numbers = []
    for number in numbers:
        number = number.lower()
        i = get_num(number)
        all_numbers.append(i)
    total_number = get_degree(all_numbers)
    return total_number


def get_info_numeral_root(root):  # word numeral to digit numeral
    # Ex:сексен алты миллион беш жүз кырк төрт миң бир жүз токсон беш = 86544195
    if len(root) > 2:
        rezult = get_info_numeral(root)
        return rezult
    else:
        return 'none'
