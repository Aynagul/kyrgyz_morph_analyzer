from analyzer.backend.analyzer.exceptions import sourceModule
def check_priority(ending_priority, priority):
    if int(priority) <= ending_priority:
        ending_priority = int(priority)
        print(ending_priority)

        return True, ending_priority
    else:
        return False, ending_priority


def check_pl(list):
    for i in list:
        if i == 'pl':
            return True
        else:
            continue

    return False


def check_tag_for_verb(tag, priority):
    if tag == sourceModule.negative:
        priority = 1
    elif tag == sourceModule.plural:
        priority = 3
    elif tag in sourceModule.possessiveness:
        priority = 4
    elif tag in sourceModule.poss_general:
        priority = 5
    elif tag in sourceModule.case:
        priority = 6
    elif tag in sourceModule.faces:
        priority = 7
    elif tag == sourceModule.ques:
        priority = 8
    elif tag == sourceModule.num_appr1:
        priority = 2
    else:
        return priority
    return priority

