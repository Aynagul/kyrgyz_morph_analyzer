different_letter = {'я':'йа',
                    'ю':'йу',
                    'ё':'йо'}
def replace_letter(word):
    for letter in word:
        if letter in different_letter:
            word = word.replace(letter, str(different_letter.get(letter)))
    return

str_continue = 'continue'
str_break = 'break'

posessiveness_general = {
    'ны', 'ни', 'ну', 'нү',
    'ды', 'ди', 'ду', 'дү',
    'ты', 'ти', 'ту', 'тү'
}
half_of_ending_for_general_possessiveness = ['кы', 'ки', 'ку', 'кү']
ending_of_gerund = ['уу','үү','оо','өө']
ending_of_gerund_pres = ['аш','ыш','иш','уш', 'үш','өш','ош']
ending_of_chakchyl = ['ып','ип','уп','үп','ап']
v_voice_all_ending = {
    'ын', 'ан', 'ун', 'үн', 'ың',   #эгин жүгүнөт
    'ыл', 'ол', 'өл', 'ул', 'үл',
    'ыш', 'иш',     #кылышты
    'аш', 'еш', 'уш', 'үш', #иштештик
    'ыр', 'ир', 'ур', 'үр',
    'ил'
}
case = ['gen','dat','acc','loc','abl']
voice = ['ref','coop','pass','caus']
mood = ['ind_pres','ind_past','ind_fut','cnd','niet','tilek']
non_finite_verb_forms = ['ger','gna_perf','ger_impf','gpr_perf','gpr_fut_neg','gpr_impf', 'gpr_pres', 'gpr_past', 'ger_pres',
                         'ger_pres']
face = ['1sg','1pl','2sg','2pl']
num_symbols = ['ord', 'top','coll','chamalama']
consonants_kg = {
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
}
special_vowel = {
    'и', 'ы', 'у', 'ү'
}
vowels_kg = {
    'а', 'о', 'ө', 'э', 'и', 'ы', 'у', 'ү', 'аа', 'оо', 'өө', 'ээ', 'уу', 'үү', 'я', 'ю', 'ё', 'е'
}
all_punctuation_marks = ['.',',','?','!','"',';',':','{','}','`']
sentence_end_p_m = ['. ','! ','? ']

half_of_ending_for_ordinal_numeral = ['чы', 'чи' , 'чу' , 'чү']
half_of_ending_for_not_sure_numeral = ['гон', 'гөн', 'ген', 'ган']

special_pronoun = ['менин','сенин','анын', 'мага','сага','ага', 'мени',
                   'сени','аны', 'анда', 'андан', 'муну', 'мунун', 'буга', 'мында', 'мындан']
prn_gen = {'менин','сенин','анын', 'мунун'}
prn_dat = {'мага','сага','ага', 'буга'}
prn_acc = {'мени','сени','аны', 'муну'}
prn_loc = {'анда', 'мында'}
prn_abl = {'андан', 'мындан'}
faces = ['1sg', '2sg', '2sgf', '1pl', '2pl', '2plf']
possessiveness = ['poss_1sg', 'poss_2sg', 'poss_2sgf', 'poss_3sg', 'poss_1pl', 'poss_2pl', 'poss_2plf']
plural = 'pl'
ques = 'ques'
agent_noun = 'agnt'
negative = 'neg'
poss_general = 'xp'
for_poss = ['1pl','poss_2pl', '2sgf', 'poss_2sgf']
all_sg = ['sg','3sg']
gerunds = ['inf_1','inf_2','inf_3','inf_4','inf_5']
chakchyl = ['advv_acc','advv_int','advv_neg','advv_suc','advv_cont']
atoochtuk = ['pcp_ps','pcp_fut_neg','pcp_pr','gpr_impf','gpr_pres']
verb_pres = ['да','до','дө']
inf1_2 = ['inf_1', 'inf_2']
for_pst_evid = ['тыр','тир','тур','түр']
advv_acc = 'advv_acc'
for_pst_evid2 = ['ып','ип','уп','үп','п']
negative_ending_verb = ['ба', 'бе', 'бө', 'бо', 'па', 'пе', 'пө', 'по']
imp_pl_1 = ['кы','ки','ку','кү','гы','ги','гу','гү']
imp_pl_2 = ['ла','ле','ло','лө']
hor_sg = ['а','е','о','ө']
two_sgf = '2sgf'
two_sgf_ending = ['ыңыз','иңиз','уңуз','үңүз']
imp_sgf = ['ңыз','ңиз','ңуз','ңүз']
inf_3 = ['ыш','иш','уш','үш','ш']
hor_pl = ['лы','ли','лу','лү']
hor_pl2 = ['лык','лик','лук','лүк']
hor_pl3 = ['алы','ели','олу','өлү','йлы','йли','йлу','йлү']
hor_pl4 = ['алык','елик','олук','өлүк','йлык','йлик','йлук','йлүк']
deside = 'deside'
deside2 = ['макчы','мекчи','мокчу','мөкчү']
inf_5_1sg = ['гым','гим','гум','гүм','кым','ким','кум','күм']
inf_5_2sg = ['гың','гиң','гуң','гүң','кың','киң','куң','күң']
pst_def = ['ты','ти','ту','тү','ды','ди','ду','дү']
neg_pres2 = ['оодо','өөдө']
neg_pre1 = ['б','п']
fut_indf = ['ар','ер','ор','өр']
fut_indf_neg = 'fut_indf_neg'
advv_int1 = ['ны','ни','ну','нү']
advv_int2 = ['га','ге','го','гө', 'ка','ке','ко','кө']
advv_neg = ['майынча','мейинче','мойунча','мөйүнчө']
num_appr1 = 'num_appr1'
advv_suc1 = ['кыча','киче','куча','күчө','гыча','гиче','гуча','гүчө']
advv_suc2 = ['ганча','генче','гончо','гөнчө','канча','кенче','кончо','көнчө']
hor_sg_str = 'hor_sg'
advv_neg2 = ['майын','мейин','мойун','мөйүн']
pst_iter = 'pst_iter'
pcp_pr = ['оочу','уучу','өөчү','үүчү']
num_appr2 = 'num_appr2'
pcp_fut_def1 = ['гыдай','гидей','гудай','гүдөй']
pcp_fut_def2 = ['чудай','чидей','чыдай','чүдөй']
pcp_fut_def3 = ['гандай','гендей','гондой','гөндөй']
gpr_pres1 = ['сан','сен','сон','сөн']
gpr_pres2 = ['максан','мексен','моксон','мөксөн']
two_sgf_verb = ['сыз','сиз','суз','сүз']
pst_def_1_sg = ['тым','тим','тум','түм','дым','дим','дум','дүм']
pst_def_2_sg = ['тың','тиң','туң','түң','дың','диң','дуң','дүң']
pst_def_1_pl = ['тык','тик','тук','түк','дык','дик','дук','дүк']
shortcut_face_1sg = 'м'
shortcut_face_2sg = 'ң'
shortcut_face_1pl = 'к'
shortcut_ending_with_1_sg = ['ам','ем','ом','өм']
fut_def_faces = ['та','те','то','тө','да','де','до','дө']
dat = 'dat'
pst_iter_1sg = ['чум','чүм']
pst_iter_2sg = ['чуң','чүң']
pst_iter_1pl = ['чук','чүк']
imp_together_tags = ['v','ques','neg','act','imp']
gerunds_together_tags = ['v','nom','gen','dat','acc','loc','abl', 'sg','pl','1sg', '2sg', '2sgf', '1pl', '2pl', '2plf',
                  '3sg','3pl','poss_1sg', 'poss_2sg', 'poss_2sgf', 'poss_3sg', 'poss_1pl', 'poss_2pl', 'poss_2plf',
                  'ques','neg','xp','imp','act']
pcp_together_tags = ['v','pl','imp','act', 'nom','gen','dat','acc','loc','abl', 'sg','pl','1sg', '2sg', '2sgf', '1pl', '2pl', '2plf',
                  '3sg','3pl','poss_1sg', 'poss_2sg', 'poss_2sgf', 'poss_3sg', 'poss_1pl', 'poss_2pl', 'poss_2plf',
                  'ques','neg','xp']
advv_together_tags = ['v','imp','act']
mood_together_tags = ['v','act','imp','neg','ques','1sg', '2sg', '2sgf', '1pl', '2pl', '2plf',
                  '3sg','3pl']
prec_1_together_tags = ['v','act','imp','neg']

opt_together_tags = ['v','act','imp','neg','1sg', '2sg', '2sgf', '1pl', '2pl', '2plf', '3sg','3pl']
advv_tags = ['advv_acc', 'advv_cont','advv_int', 'advv_neg','advv_suc']
gerunds_tags = ['inf_1','inf_2','inf_3','inf_4','inf_5']
pcp_tags = ['pcp_pr','pcp_ps','pcp_fut_def','pcp_fut_neg','gpr_pres']
verb_mood = ['pres','pst_def','pst_indf','pst_evid','pst_iter','fut_def', 'fut_indf','fut_indf_neg','cond','deside']
imp_tags = ['imp_sg', 'imp_sgf', 'imp_pl', 'imp_plf', 'jus_sg', 'jus_pl']
tags_with_noun = ['n','nom','gen','dat','acc','loc','abl', 'sg','pl','1sg', '2sg', '2sgf', '1pl', '2pl', '2plf',
                  '3sg','3pl','poss_1sg', 'poss_2sg', 'poss_2sgf', 'poss_3sg', 'poss_1pl', 'poss_2pl', 'poss_2plf',
                  'ques','agnt','neg','xp']
fut_def_special = ['йм']
fut_def_special_negative = ['бай', 'бей', 'бөй', 'бой', 'пай', 'пей', 'пөй', 'пой']
cond_1sg = ['сам','сем','сом','сөм']
cond_2sg = ['саң','сең','соң','сөң']
cond_1pl = ['сак','сек','сок','сөк']
optative_mood_1sg_1pl = ['hor_sg','hor_pl']
hor_together_tags = ['v','ques','neg']
inf_1_inf_2_with_shortcut_faces = ['оом','уум','өөм','үүм', 'ооң','ууң','өөң','үүң']
inf_1_with_shortcut_1sg = ['оом', 'өөм']
inf_2_with_shortcut_1sg = ['уум', 'үүм']
inf_1_with_shortcut_2sg = ['ооң', 'өөң']
inf_2_with_shortcut_2sg = ['ууң', 'үүң']
poss_1sg_2sg = ['poss_1sg', 'poss_2sg']
advv_acc_latest_letter = 'п'
