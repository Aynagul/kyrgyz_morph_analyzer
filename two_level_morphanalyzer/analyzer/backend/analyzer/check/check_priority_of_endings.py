
def check_priority(ending_priority, priority):
    if int(priority) <= ending_priority:
        ending_priority = int(priority)
        print(ending_priority)
        return True, ending_priority
    else:
        return False, ending_priority


def check_pl(list):
    print(list)
    for i in list:
        if i == 'pl':
            return True
        else:

            continue

    return False