from analyzer.backend.analyzer.exceptions import sourceModule

def check_tags2(list, list2, sym):
    list.remove(sym)
    for tag in list:
        if tag not in list2:
            return False
        else:
            continue
    list.append(sym)
    return True

def check_tags(tag_list, wrong_word):
    tag_list = list(dict.fromkeys(tag_list))  # delete duplicates symbols
    tag_list = [i for i in tag_list if i is not None]
    print(tag_list)
    if wrong_word:
        return True, tag_list
    else:
        for tag in tag_list:
            if tag in sourceModule.imp_tags and check_tags2(tag_list, sourceModule.imp_together_tags, tag):
                return False, tag_list
            elif tag in sourceModule.pcp_tags and check_tags2(tag_list, sourceModule.pcp_together_tags, tag):
                return False, tag_list
            elif tag in sourceModule.verb_mood and check_tags2(tag_list, sourceModule.mood_together_tags, tag):
                return False, tag_list
            elif tag in sourceModule.gerunds_tags and check_tags2(tag_list, sourceModule.gerunds_together_tags, tag):
                return False, tag_list
            elif tag in sourceModule.advv_tags and check_tags2(tag_list, sourceModule.advv_together_tags, tag):
                return False, tag_list
            elif tag in sourceModule.optative_mood_1sg_1pl and check_tags2(tag_list, sourceModule.hor_together_tags, tag):
                return False, tag_list
            elif tag == 'opt' and check_tags2(tag_list, sourceModule.opt_together_tags, tag):
                return False, tag_list
            elif tag == 'prec_1' and check_tags2(tag_list, sourceModule.prec_1_together_tags, tag):
                return False, tag_list
            elif tag == 'v' or tag == 'act' or tag == 'imp':
                continue

            elif tag == 'neg':
                continue
            elif tag in sourceModule.numeral_tags and check_tags2(tag_list, sourceModule.tags_with_numeral, tag):
                return False, tag_list
            elif tag in sourceModule.adj_tags and check_tags2(tag_list, sourceModule.tags_with_adj, tag):
                return False, tag_list
            elif tag == 'n':
                wrong_word = False
                break
            elif tag == 'num' or tag == 'num_card':
                continue
            elif tag == 'adj' or tag == 'pst':
                continue
            else:
                wrong_word = True
                break
    if wrong_word:
        return True, tag_list
    else:
        return False, tag_list