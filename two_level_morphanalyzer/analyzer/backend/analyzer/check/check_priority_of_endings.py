from analyzer.backend.analyzer.exceptions import sourceModule
def check_priority(ending_priority, priority):
    if int(priority) <= ending_priority:
        ending_priority = int(priority)
        return True, ending_priority
    else:
        return False, ending_priority

def check_prec_1(list):
    for i in list:
        if i == 'prec_1':
            return True
        else:
            continue

    return False
def check_change_ending(tags_list):
    tags_list = list(dict.fromkeys(tags_list))  # delete duplicates symbols
    tags_list = [i for i in tags_list if i is not None]
    for j in tags_list:
        if j in sourceModule.change_tags_without_faces:
            return True
        else:
            continue

    return False

def check_pl(list):
    for i in list:
        if i == 'pl':
            return True
        else:
            continue

    return False

def check_px2sgf(list):
    print(list)
    for i in list:
        if i == 'px2sgf':
            return True
        else:
            continue

    return False

def check_2pl(list):
    for i in list:
        if i == 'p2pl':
            return True
        else:
            continue

    return False

def check_2plf(list):
    for i in list:
        if i == 'p2plf':
            return True
        else:
            continue

    return False


def check_faces(list):
    for i in list:
        if i in sourceModule.faces:
            return True
        else:
            continue

    return False

def check_tag_for_verb(tag, priority, list):
    if tag == sourceModule.neg_str:
        priority = 1
    elif tag == sourceModule.plural:
        priority = 3
    elif tag in sourceModule.possessiveness:
        priority = 4
    elif tag in sourceModule.poss_general:
        priority = 5
    elif tag in sourceModule.case and check_2pl(list):
        priority = 2
    elif tag in sourceModule.case and check_2plf(list):
        priority = 2
    elif tag in sourceModule.case:
        priority = 6
    elif tag in 'p2sgf' and check_pl(list):
        priority = 3
    elif tag in sourceModule.faces:
        priority = 7
    elif tag == sourceModule.ques:
        priority = 8
    elif tag == sourceModule.num_appr1:
        priority = 2
    else:
        return priority
    return priority

def check_tag_for_numeral(tag, priority, list):
    if tag == sourceModule.neg_str:
        priority = 5
    elif tag == sourceModule.plural:
        priority = 2
    elif tag in sourceModule.possessiveness:
        priority = 3
    elif tag in sourceModule.poss_general:
        priority = 4
    elif tag == 'abl':
        priority = 1
    elif tag == 'past_indf':
        priority = 1
    elif tag == 'imp':
        return 'px2sgf', 2
    elif tag in sourceModule.case:
        priority = 5
    elif tag in sourceModule.faces:
        priority = 6
    elif tag == sourceModule.ques:
        priority = 7
    elif tag == sourceModule.num_appr1:
        priority = 2
    else:
        return tag, priority
    return tag, priority


def check_tag_for_adj(tag, priority, list):
    if tag == sourceModule.neg_str:
        priority = 5
    elif tag == sourceModule.plural:
        priority = 2
    elif tag in sourceModule.possessiveness:
        priority = 3
    elif tag in sourceModule.poss_general:
        priority = 4
    elif tag in sourceModule.case:
        priority = 5
    elif tag in sourceModule.faces:
        priority = 6
    elif tag == sourceModule.ques:
        priority = 7
    elif tag == 'imp':
        return 'px2sgf', 2
    else:
        return tag, priority
    return tag, priority

def change_tag_for_verb(tag, ending):
    if ending in sourceModule.two_sgf_verb:
        tag = 'p2sgf'
        return tag
    elif tag == 'px1pl':
        tag = 'p1pl'
        return tag
    else:
        return tag

def change_tag_for_noun(tag, priority):
    if tag == 'num_top':
        return 'abl', 4
    elif tag == 'imp':
        return 'px2sgf', 2
    else:
        return tag, priority

def change_tag_for_num(tag, priority):
    if tag == 'imp':
        return 'px2sgf', 2
    else:
        return tag, priority