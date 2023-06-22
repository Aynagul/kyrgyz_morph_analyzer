from analyzer.backend.work_with_db.find_endings import find_endings
from analyzer.backend.analyzer.check import check_punctuation_marks, check_special_pronouns, check_priority_of_endings, check_tags
from analyzer.backend.analyzer.exceptions import sourceModule
from analyzer.backend.analyzer.block import block_of_noun, block_of_verb, block_of_numeral, block_of_adjective, common
from analyzer.backend.analyzer.block.common import listToString
from analyzer.backend.analyzer.block.common import convertTuple
from analyzer.backend.analyzer.endings import Noun, Cases, Faces, Others, Adverb, Possessiveness, Adjectives_2, Numeral, \
    Pronoun, Verb

def numeral_analyzer(self, str_ending, index, new_list, ending, ending_list, new_word, ending_priority, symbols_list, symbols):
    print('numeral block')
    str_ending = (str_ending,)
    symbol, priority = find_endings(str_ending)
    if symbol:
<<<<<<< HEAD

        symbol, priority = check_priority_of_endings.check_tag_for_numeral(symbol, priority, symbols_list)
=======
        priority = check_priority_of_endings.check_tag_for_numeral(symbol, priority, symbols_list)
>>>>>>> master
        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(ending_priority, priority)
        if is_correct_priority:
            print('correct prio')
            if symbol in sourceModule.faces:
                new_list, new_word, self.__symbols_list, self.__symbols = \
                    common.faces(index, new_list, symbol, convertTuple(str_ending), symbols_list, symbols)

            elif symbol == sourceModule.pst_iter_str or symbol == sourceModule.prec_1_str:
                print('block ынчы')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_numeral.num_ord(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
                return '', new_list, new_word, ending_priority
            elif symbol == sourceModule.abl_str:
                print('block тан')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_numeral.num_top(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
                return '', new_list, new_word, ending_priority
<<<<<<< HEAD
            elif symbol == sourceModule.past_indf:
=======
            elif symbol == sourceModule.pst_indf:
>>>>>>> master
                print('block num_appr3')
                new_list, new_word, self.__symbols, self.__symbols_list = block_of_numeral.num_appr3(
                    self, convertTuple(str_ending), new_list, index, new_word, symbols,
                    symbols_list)
                return '', new_list, new_word, ending_priority
            elif symbol == sourceModule.num_appr1:
                print('cha')
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol == sourceModule.num_appr2:
                print('дай')
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol in sourceModule.case:
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))
            elif symbol in sourceModule.possessiveness:
                print(33)
                new_list, new_word, self.__symbols_list, self.__symbols = \
                    common.possessiveness(index, new_list, symbol, convertTuple(str_ending), symbols_list,
                                          symbols)
            elif symbol == sourceModule.plural or symbol == sourceModule.ques or symbol == sourceModule.agent_noun \
<<<<<<< HEAD
                    or symbol == sourceModule.neg_str:
=======
                    or symbol == sourceModule.negative:
>>>>>>> master
                new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                    common.common_exception_11(index, new_list, symbol, convertTuple(str_ending), symbols_list,
                                               symbols, ending_priority)

                # new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))

<<<<<<< HEAD
            elif symbol == 'fut_aor':
=======
            elif symbol == 'opt':
>>>>>>> master
                # for posessiveness_general (ныкы) итд
                ending_priority = 3
                new_list, index, last_letter, str = \
                    common.common_exception_1(new_list, convertTuple(str_ending))
                if ending in sourceModule.half_of_ending_for_general_possessiveness and new_list[
                    index - 1] in sourceModule.posessiveness_general:
                    new_list, index, ending, ending_list = common.common_exception_2(index, new_list,
                                                                                     convertTuple(str_ending),
                                                                                     ending_list, str)
                    return sourceModule.str_continue, new_list, new_word, ending_priority
            elif symbol == 'xp':
                new_list, new_word = common.common(self, index, new_list, symbol, convertTuple(str_ending))

            return '', new_list, new_word, ending_priority

        elif symbol in sourceModule.for_poss and check_priority_of_endings.check_pl(self.__symbols_list):

            self.__wrong_priority = True
            return sourceModule.str_break, new_list, new_word, ending_priority
        elif symbol in sourceModule.for_poss:
            if symbol in sourceModule.faces:
                new_list, new_word, self.__symbols_list, self.__symbols = \
                    common.faces(index, new_list, symbol, convertTuple(str_ending), symbols_list, symbols)
            return '', new_list, new_word, ending_priority


<<<<<<< HEAD
        elif symbol in sourceModule.neg_str and check_priority_of_endings.check_pl(self.__symbols_list):
=======
        elif symbol in sourceModule.negative and check_priority_of_endings.check_pl(self.__symbols_list):
>>>>>>> master
            new_list, new_word, self.__symbols_list, self.__symbols, ending_priority = \
                common.common_exception_11(index, new_list, symbol, convertTuple(str_ending),
                                           symbols_list,
                                           symbols, ending_priority)
            return '', new_list, new_word, ending_priority
        else:
            self.__wrong_priority = True
            return sourceModule.str_break, new_list, new_word, ending_priority
    else:
<<<<<<< HEAD
        print(convertTuple(str_ending))
        if convertTuple(str_ending)[-1] in sourceModule.shortcut_poss_3sg_ending:
            print('px2sgf, px3sg, px1pl, px2plf with pl')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_noun.poss(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            print(new_word)
            return '', new_list, new_word, ending_priority
        elif convertTuple(str_ending)[-1] in sourceModule.shortcut_ending_poss:
            print('м, ң')
            new_list, new_word, self.__symbols, self.__symbols_list = block_of_noun.short_poss_ending(
                self, convertTuple(str_ending), new_list, index, new_word, symbols,
                symbols_list)
            print(new_word)
            return '', new_list, new_word, ending_priority
=======

        new_list, index, last_letter, str = \
            common.common_exception_1(new_list, convertTuple(str_ending))

        if len(ending) == 2 and last_letter in sourceModule.special_vowel:

            if not self.__symbols:
                new_list, index, ending, ending_list, index2 = common.common_exception_3 \
                    (index, new_list, convertTuple(str_ending), ending_list, str)
                if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                    priority = 2
                    is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                        ending_priority, priority)
                    if is_correct_priority:
                        new_list[index] = str[1:]
                        str = str.replace(str[1:], '')
                        new_list, new_word, self.__symbols, self.__symbols_list = common.common_exception_4(new_list,
                                                                                                            symbol,
                                                                                                            last_letter,
                                                                                                            str,
                                                                                                            symbols,
                                                                                                            symbols_list)
                        if self.find_root_from_the_end(new_word):
                            return sourceModule.str_break, new_list, new_word, ending_priority
                        else:
                            new_list.reverse()
                            new_word = listToString(new_list)
                            if self.find_root_from_the_end(new_word):
                                return sourceModule.str_break, new_list, new_word, ending_priority
                            else:
                                return sourceModule.str_continue, new_list, new_word, ending_priority
                    else:
                        self.__wrong_priority = True
                        return sourceModule.str_break, new_list, new_word, ending_priority
            else:
                is_px3sp = True
                for key in list(self.__symbols.keys()):  # ыңар, ыбыз, ыңыз
                    if key in Possessiveness.posessiveness_2st_sg_politely or key in Possessiveness.posessiveness_1st_pl or key \
                            in Possessiveness.posessiveness_2st_pl:
                        priority = 2
                        ending_priority = 4
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                            ending_priority, priority)
                        is_px3sp = False
                        if is_correct_priority:
                            index, new_list, last_letter, ending, self.__symbols, ending_list = \
                                common.common_exception_5(index, new_list, last_letter,
                                                          convertTuple(str_ending),
                                                          symbols, ending_list, str)
                        else:
                            self.__wrong_priority = True
                            return sourceModule.str_break, new_list, new_word, ending_priority
                    else:
                        return sourceModule.str_continue, new_list, new_word, ending_priority
                # px3sp with other endings
                if is_px3sp:
                    new_list, ending_list = common.common_exception_6(index, new_list,
                                                                      convertTuple(str_ending),
                                                                      ending_list, str)
                    if (symbol := Possessiveness.get_info_possessive(last_letter)) != 'none':
                        priority = 2
                        is_correct_priority, ending_priority = check_priority_of_endings.check_priority(
                            ending_priority, priority)
                        if is_correct_priority:
                            new_list, ending_list = common.common_exception_4(index, new_list,
                                                                              convertTuple(str_ending),
                                                                              ending_list, str)
                            if self.find_root_from_the_end(new_word):
                                return sourceModule.str_break, new_list, new_word, ending_priority
                            else:
                                new_list.reverse()
                                new_word = listToString(new_list)
                                if self.find_root_from_the_end(new_word):
                                    return sourceModule.str_break, new_list, new_word, ending_priority
                                else:
                                    return sourceModule.str_continue, new_list, new_word, ending_priority
                        else:
                            self.__wrong_priority = True
                            return sourceModule.str_break, new_list, new_word, ending_priority

                else:  # ыңар, ыбыз, ыңыз
                    new_word = listToString(new_list)
                    if self.find_root_from_the_end(new_word):
                        return sourceModule.str_break, new_list, new_word, ending_priority
                    else:
                        new_list.reverse()
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            return sourceModule.str_break, new_list, new_word, ending_priority
                        else:
                            return sourceModule.str_continue, new_list, new_word, ending_priority
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
                        return sourceModule.str_break, new_list, new_word, ending_priority
                    else:
                        new_list.reverse()
                        new_word = listToString(new_list)
                        if self.find_root_from_the_end(new_word):
                            return sourceModule.str_break, new_list, new_word, ending_priority
                        else:
                            return sourceModule.str_continue, new_list, new_word, ending_priority
                else:
                    self.__wrong_priority = True
                    return sourceModule.str_break, new_list, new_word, ending_priority
            else:
                return sourceModule.str_continue, new_list, new_word, ending_priority
>>>>>>> master
