from analyzer.backend.analyzer.exceptions import sourceModule

def check_tags2(list, list2, sym):
    print(list)
    list.remove(sym)
    for tag in list:
        if tag not in list2:
            return False
        else:
            continue
    return True

def check_tags(tag_list):
    tag_list = list(dict.fromkeys(tag_list))  # delete duplicates symbols
    tag_list = [i for i in tag_list if i is not None]
    print(tag_list)
    for tag in tag_list:
        if tag in sourceModule.imp_tags and check_tags2(tag_list, sourceModule.imp_together_tags, tag):
            return False, tag_list
    return True, tag_list