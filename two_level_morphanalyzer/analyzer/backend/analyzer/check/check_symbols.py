from analyzer.backend.analyzer.exceptions import sourceModule

def get_faces_tag(list):
    for tag in list:
        if tag in sourceModule.faces:
            return True
        else:
            continue
    return False
def delete_symbols(sym_list, symbol):
    if symbol == 'nom' in sym_list and [sym for sym in sourceModule.case if (sym in sym_list)]:
        sym_list.remove('nom')
<<<<<<< HEAD
    elif symbol == 'p3sg' in sym_list and [sym for sym in sourceModule.plural if (sym in sym_list)]:
        sym_list.remove('p3sg')
=======
    elif symbol == '3sg' in sym_list and [sym for sym in sourceModule.plural if (sym in sym_list)]:
        sym_list.remove('3sg')
>>>>>>> master
    elif symbol == 'act' in sym_list and [sym for sym in sourceModule.voice if (sym in sym_list)]:
        sym_list.remove('act')
    elif symbol == 'imp' in sym_list and [sym for sym in sourceModule.mood if (sym in sym_list)]:
        sym_list.remove('imp')
<<<<<<< HEAD
    elif symbol == 'p3sg' in sym_list and [sym for sym in sourceModule.faces if (sym in sym_list)]:
        sym_list.remove('p3sg')
    elif symbol == 'cnd' in sym_list:
        res = get_faces_tag(sym_list)
        if not res:
            sym_list.append('p3sg')
    elif symbol == 'num_card' in sym_list and [sym for sym in sourceModule.num_symbols if (sym in sym_list)]:
        sym_list.remove('num_card')
    elif symbol == 'pst' in sym_list and [sym for sym in sourceModule.adj_ending_tags if (sym in sym_list)]:
        sym_list.remove('pst')
=======
    elif symbol == '3sg' in sym_list and [sym for sym in sourceModule.faces if (sym in sym_list)]:
        sym_list.remove('3sg')
    elif symbol == 'cond' in sym_list:
        res = get_faces_tag(sym_list)
        if not res:
            sym_list.append('3sg')
    elif symbol == 'num_card' in sym_list and [sym for sym in sourceModule.num_symbols if (sym in sym_list)]:
        sym_list.remove('num_card')
>>>>>>> master
    elif symbol == 'num' in sym_list and [sym for sym in sourceModule.part_of_speech_tags if (sym in sym_list)]:
        sym_list.remove('post')
    elif symbol == 'imp' in sym_list and [sym for sym in sourceModule.non_finite_verb_forms if (sym in sym_list)]:

        sym_list.remove('imp')
    elif symbol == 'act' in sym_list and [sym for sym in sourceModule.non_finite_verb_forms if
                                                     (sym in sym_list)]:
        sym_list.remove('act')
<<<<<<< HEAD
=======
        sym_list.remove('pass')
>>>>>>> master
    return sym_list