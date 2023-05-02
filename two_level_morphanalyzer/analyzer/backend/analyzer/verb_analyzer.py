from analyzer.backend.work_with_db.find_endings import find_endings
from analyzer.backend.analyzer.check import check_punctuation_marks, check_special_pronouns, check_priority_of_endings, check_tags
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.analyzer.block import block_of_noun, block_of_verb, block_of_numeral, block_of_adjective, common
from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.block.common import convertTuple
from analyzer.backend.analyzer.endings import Noun, Cases, Faces, Others, Adverb, Possessiveness, Adjectives_2, Numeral, \
    Pronoun, Verb

def verb_analyzer(self, str_ending, index, new_list, ending, ending_list, new_word, ending_priority, symbols_list, symbols):
    print('verb block')
    str_ending = (str_ending,)
    symbol, priority = find_endings(str_ending)
    print(new_list)
    if symbol:
        symbol = check_priority_of_endings.change_tag_for_verb(symbol, convertTuple(str_ending))
        priority = check_priority_of_endings.check_tag_for_verb(symbol, priority, symbols_list)

        print('priority:{}'.format(priority))
        print(symbol)
        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(ending_priority,
                                                                                        priority)

        if is_correct_priority:
            if symbol in sourceModule.faces:
                self.__is_like_a_noun = True
                new_list, new_word, self.__symbols_list, self.__symbols = \
                    block_of_verb.faces_for_verb(self, index, new_list, symbol, convertTuple(str_ending),
                                                 symbols_list,
                                                 symbols, new_word)
            elif symbol == sourceModule.deside:
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.deside(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
            elif symbol == sourceModule.hor_sg_str:
                print('йын')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.advv_neg2(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list, symbol)
            elif symbol == sourceModule.pst_iter:
                print('chu')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.pcp_pr(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list, symbol)
            elif symbol == sourceModule.num_appr1:
                print('cha')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.advv_neg(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
            elif symbol == sourceModule.num_appr2:
                print('дай')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.pcp_fut_def(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
            elif symbol in sourceModule.gerunds:
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol in sourceModule.chakchyl:
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol in sourceModule.atoochtuk:
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol in sourceModule.case:
                print(11)
                self.__is_like_a_noun = True
                if convertTuple(str_ending) in sourceModule.fut_def_faces and check_priority_of_endings.check_faces(
                        symbols_list):

                    new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.fut_def_faces(
                        self, convertTuple(str_ending), new_list, index, new_word, symbols,
                        symbols_list)

                    print(new_word)
                elif convertTuple(str_ending) in sourceModule.pst_def:

                    new_list, new_word = block_of_verb.pst_def(self, convertTuple(str_ending), new_list, index)
                    print(new_word)
                elif convertTuple(str_ending) in sourceModule.advv_int1:
                    new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.advv_int(
                        self, convertTuple(str_ending), new_list, index, new_word, symbols,
                        symbols_list)
                else:
                    new_list, new_word = common.common(self, index, new_list, symbol,
                                                       convertTuple(str_ending))

                if self.find_root_from_the_end(new_word):
                    return sourceModule.str_break, new_list, new_word, ending_priority
                else:
                    new_list.reverse()
                    print(new_list)
                    return sourceModule.str_continue, new_list, new_word, ending_priority
            elif symbol in sourceModule.possessiveness:
                print('poss block')
                self.__is_like_a_noun = True
                new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                    block_of_verb.possessiveness_for_verb(self, index, new_list, symbol, convertTuple(str_ending),
                                                          symbols_list,
                                                          symbols, new_word)
            elif symbol == sourceModule.plural:
                print(new_list)
                new_word, new_list = block_of_verb.pl(self, convertTuple(str_ending), new_list, index, symbol, new_word)

                if self.find_root_from_the_end(new_word):
                    return sourceModule.str_break, new_list, new_word, ending_priority
                else:
                    new_list.reverse()
                    print(new_list)
                    return sourceModule.str_continue, new_list, new_word, ending_priority
            elif symbol == sourceModule.negative:
                is_fut_indf_neg, new_list, new_word = block_of_verb.fut_indf_neg_with_neg(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbol)
                if is_fut_indf_neg:
                    self.__wrong_priority = True
                    return sourceModule.str_break, new_list, new_word, ending_priority
                # new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol == sourceModule.ques or symbol == sourceModule.agent_noun:
                print(12)

                new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                    block_of_verb.common_exception_for_verb(index, new_list, symbol, convertTuple(str_ending),
                                                            symbols_list,
                                                            symbols, ending_priority)
                print(new_word)
            elif symbol == 'opt' and new_list[1] in sourceModule.posessiveness_general:
                # for posessiveness_general (ныкы) итд
                ending_priority = 5
                new_list, index, last_letter, str = \
                    common.common_exception_1(new_list, convertTuple(str_ending))
                if ending in sourceModule.half_of_ending_for_general_possessiveness and new_list[
                    index - 1] in sourceModule.posessiveness_general:
                    new_list, index, ending, ending_list = common.common_exception_2(index, new_list,
                                                                                     convertTuple(
                                                                                         str_ending),
                                                                                     ending_list, str)
                    return sourceModule.str_continue, new_list, new_word, ending_priority
            elif symbol == 'xp':
                self.__is_like_a_noun = True
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            else:
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))


            return '', new_list, new_word, ending_priority


        elif symbol in sourceModule.possessiveness and check_priority_of_endings.check_pl(symbols_list):
            print('poss block with pl')
            self.__is_like_a_noun = True
            new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                block_of_verb.possessiveness_for_verb(self, index, new_list, symbol,
                                                      convertTuple(str_ending),
                                                      symbols_list,
                                                      symbols, new_word)
            return '', new_list, new_word, ending_priority
        elif symbol in sourceModule.case and block_of_verb.is_hor_sg(symbols_list):
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.hor_sg(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif symbol in sourceModule.for_poss and check_priority_of_endings.check_pl(symbols_list):
            self.__is_like_a_noun = True
            new_word, new_list, self.__symbols, self.__symbols_list = block_of_verb.imp_plf(self, index, new_list,
                                                                                            convertTuple(str_ending),
                                                                                            new_word, symbols,
                                                                                            symbols_list)
            return '', new_list, new_word, ending_priority
        elif symbol in sourceModule.for_poss:
            if symbol in sourceModule.faces:
                self.__is_like_a_noun = True
                new_list, new_word, self.__symbols_list, self.__symbols = \
                    common.faces(index, new_list, symbol, convertTuple(str_ending), symbols_list,
                                 symbols)
            return '', new_list, new_word, ending_priority


        elif symbol in sourceModule.negative and check_priority_of_endings.check_pl(symbols_list):
            self.__is_like_a_noun = True
            new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                           symbols_list,
                                           symbols, ending_priority)
            return '', new_list, new_word, ending_priority
        else:
            print(symbols_list)
            print(symbols)
            self.__wrong_priority = True
            return sourceModule.str_break, new_list, new_word, ending_priority
    else:
        print(convertTuple(str_ending))
        if convertTuple(str_ending)[-1] == 'р' and self.find_root_from_the_end(
                new_word[:-1]):
            print('ar')
            new_list, new_word = block_of_verb.fut_indf(self, convertTuple(str_ending), new_list)
            print(new_word)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending)[-1] == 'р' and convertTuple(str_ending)[:-1] in sourceModule.negative_ending_verb \
                and self.find_root_from_the_end(new_word[:-3]):
            print('bar')
            new_list, new_word = block_of_verb.fut_indf_neg(self, convertTuple(str_ending), new_list, index)
            return '', new_list, new_word, ending_priority


        elif convertTuple(str_ending) in sourceModule.gpr_pres1:
            print('gpr_pres')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.gpr_pres(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.hor_pl or convertTuple(str_ending) in sourceModule.hor_pl2:
            print('hor_pl')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.hor_pl(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.pst_iter_1sg or convertTuple(
                str_ending) in sourceModule.pst_iter_2sg \
                or convertTuple(str_ending) in sourceModule.pst_iter_1pl:
            print('pst_iter_with_faces')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.pst_iter_faces(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending)[-1] in sourceModule.hor_sg and block_of_verb.is_hor_sg(symbols_list):
            print('ayin')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.hor_sg(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.imp_pl_2:
            print('gyla')
            print(14)
            new_list, new_word = block_of_verb.imp_pl(self, convertTuple(str_ending), new_list, index, new_word)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.inf_5_1sg or convertTuple(str_ending) in sourceModule.inf_5_2sg:
            print('гым, гың')
            new_list, new_word = block_of_verb.inf_5(self, convertTuple(str_ending), new_list, index, new_word)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.pst_def_1_sg or convertTuple(
                str_ending) in sourceModule.pst_def_2_sg \
                or convertTuple(str_ending) in sourceModule.pst_def_1_pl:
            print('дим...')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.pst_def_face(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.cond_2sg \
                or convertTuple(str_ending) in sourceModule.cond_1pl:
            print('cond with faces')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.cond_faces(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending)[1:] in sourceModule.shortcut_ending_with_1_sg:
            print('fut_def with 1sg and cond with 1sg')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.shortcut_ending_with_1_sg(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending) in sourceModule.fut_def_special_negative:
            print('fut_def with faces and neg')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.fut_def_special_negative(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending)[2] == sourceModule.advv_acc_latest_letter:
            print('чуркап')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.advv_acc_latest_letter(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif len(convertTuple(str_ending)) == 4 and convertTuple(str_ending)[
                                                    1:] in sourceModule.inf_1_inf_2_with_shortcut_faces:
            print('inf_1_inf_2_with_shortcut_faces')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.inf_1_inf_2_with_shortcut_faces(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority
        elif len(convertTuple(str_ending)) == 4 and convertTuple(str_ending)[2:] in sourceModule.fut_def_special:
            print('fut_def_1sg and with neg')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.fut_def_special(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            return '', new_list, new_word, ending_priority

        strip_ending = convertTuple(str_ending)[1:]
        strip_ending = (strip_ending,)
        symbol, priority = find_endings(strip_ending)
        print(12)
        if symbol:
            # if strip_ending in sourceModule.ending_of_gerund or strip_ending in sourceModule.ending_of_gerund_pres:

            # if (symbol := Verb.get_gerund(strip_ending)) != 'none':
            # priority = 2
            priority = check_priority_of_endings.check_tag_for_verb(symbol, priority, symbols_list)
            is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                ending_priority, priority)
            if is_correct_priority:
                print('strip block')
                print(symbol)
                if symbol in sourceModule.inf1_2:
                    print(11)
                    is_loc, ending, self.__symbols, self.__symbols_list = block_of_verb.is_ending_a_loc(symbols,
                                                                                                        symbols_list)
                    if is_loc:
                        print('uuda')
                        print(symbols)
                        new_list, new_word = block_of_verb.special_pres(self,
                                                                        convertTuple(str_ending),
                                                                        index, new_list, ending, new_word)
                        print(new_word)
                        return '', new_list, new_word, ending_priority
                    else:
                        new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.special_gerund(self,
                                                                                                               convertTuple(
                                                                                                                   str_ending),
                                                                                                               symbol,
                                                                                                               index,
                                                                                                               new_list,
                                                                                                               symbols,
                                                                                                               symbols_list)
                        return '', new_list, new_word, ending_priority
                elif symbol == sourceModule.dat and check_priority_of_endings.check_faces(symbols_list):
                    new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.fut_def_faces(
                        self, convertTuple(str_ending), new_list, index, new_word, symbols,
                        symbols_list)
                elif symbol in sourceModule.poss_1sg_2sg:
                    new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.inf_3_poss(
                        self, convertTuple(str_ending), new_list, index, new_word, symbols,
                        symbols_list, symbol)
                else:
                    print('yp, ysh, uu')
                    new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.special_gerund(self,
                                                                                                           convertTuple(
                                                                                                               str_ending),
                                                                                                           symbol,
                                                                                                           index,
                                                                                                           new_list,
                                                                                                           symbols,
                                                                                                           symbols_list)
                print(new_word)
                return '', new_list, new_word, ending_priority
            else:
                self.__wrong_priority = True
                return sourceModule.str_break, new_list, new_word, ending_priority
        else:
            if convertTuple(str_ending) in sourceModule.for_pst_evid:
                is_pst_evid, new_list, new_word = block_of_verb.is_ending_a_pst_evid(
                    self, new_list, index, convertTuple(str_ending), new_word)
                if is_pst_evid:
                    return '', new_list, new_word, ending_priority
            elif convertTuple(str_ending)[-1] in sourceModule.inf_3:
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_verb.inf_3(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols, symbols_list)
                return '', new_list, new_word, ending_priority
            else:
                new_list, new_word = block_of_verb.special_gerund(self, convertTuple(str_ending),
                                                                  symbol, index, new_list, symbols, symbols_list)
        if convertTuple(str_ending)[-1] == 'п' and self.find_root_from_the_end(
                self.__word_without_punctuation.lower()[:-1]):
            priority = 2
            is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                ending_priority, priority)
            if is_correct_priority:
                new_list, new_word = block_of_verb.special_chakchyl_1(self, ending, index, new_list)
                return '', new_list, new_word, ending_priority
            else:
                self.__wrong_priority = True
                return sourceModule.str_break, new_list, new_word, ending_priority
        '''
        new_list, index, last_letter, str = common.common_exception_1(new_list, convertTuple(str_ending))
        
        if len(ending) == 2 and last_letter in sourceModule.special_vowel:

            if not self.__symbols:
                new_list, index, ending, ending_list, index2 = common.common_exception_3(index, new_list, convertTuple(str_ending), ending_list, str)
                if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                    priority = 4
                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                        ending_priority, priority)
                    if is_correct_priority:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        new_list, new_word, self.__symbols, self.__symbols_list = common.common_exception_4(
                            new_list, symbol, last_letter, str, self.__symbols, self.__symbols_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            new_list.reverse()
                            new_word = listToString(new_list)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                continue
                    else:
                        self.__wrong_priority = True
                        break
            else:
                is_px3sp = True
                for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                    if key in Possessiveness.posessiveness_2st_sg_politely or key in Possessiveness.posessiveness_1st_pl or key in Possessiveness.posessiveness_2st_pl:
                        priority = 4
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                            ending_priority, priority)
                        is_px3sp = False
                        if is_correct_priority:
                            index, new_list, last_letter, ending, self.__symbols, ending_list = common.common_exception_5(index, new_list, last_letter,
                                                          convertTuple(str_ending),
                                                          self.__symbols, ending_list, str)
                        else:
                            self.__wrong_priority = True
                            break
                    else:
                        continue
                # px3sp with other endings
                if is_px3sp:
                    new_list, ending_list = common.common_exception_6(index, new_list,
                                                                      convertTuple(str_ending),
                                                                      ending_list, str)
                    if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                        priority = 4
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                            ending_priority, priority)
                        if is_correct_priority:
                            new_list, ending_list = common.common_exception_4(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)
                            if self.find_root_from_the_end(new_word):
                                break
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    break
                                else:
                                    continue
                        else:
                            self.__wrong_priority = True
                            break

                else:  # ыңар, ыбыз, ыңыз
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            continue
        # for px1sg(ым) and px2sg(ың)
        else:
            new_list[index] = str[1:]
            str = str.replace(str[1:], '')
            try:
                new_list, ending_list = common.common_exception_8(index, new_list,
                                                                  convertTuple(str_ending),
                                                                  ending_list, str)

            except:
                new_list, ending_list = common.common_exception_9(index, new_list,
                                                                  convertTuple(str_ending),
                                                                  ending_list, str)
            str = listToString(new_list[index])
            str = (str,)
            symbol, priority = find_endings(str)
            if symbol:
                is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                    ending_priority, priority)
                if is_correct_priority:
                    new_list, new_word = common.common_exception_10(self, new_list,
                                                                    symbol, convertTuple(str))
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            break
                        else:
                            continue
                else:
                    self.__wrong_priority = True
                    break
            else:
                continue'''