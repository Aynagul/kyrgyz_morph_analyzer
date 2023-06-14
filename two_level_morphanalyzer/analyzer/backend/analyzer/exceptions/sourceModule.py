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
mood = ['pres','past_def','past_indf','past_evid','past_iter','fut_def', 'fut_aor','fut_indf_neg','cnd','fut_indf']
non_finite_verb_forms = ['ger','gna_perf','ger_impf','gpr_perf','gpr_fut_neg','gpr_impf', 'gpr_pres', 'gpr_past', 'ger_pres',
                         'ger_pres']
face = ['p1sg','p1pl','p2sg','p2pl']
num_symbols = ['num_ord', 'num_top','num_appr1','num_appr2', 'num_appr3']
consonants_kg = {
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'ң', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
}
special_vowel = {
    'и', 'ы', 'у', 'ү'
}
vowels_kg = {
    'а', 'о', 'ө', 'э', 'и', 'ы', 'у', 'ү', 'аа', 'оо', 'өө', 'ээ', 'уу', 'үү', 'я', 'ю', 'ё', 'е'
}
narrow_vowels = ['э','е','и','ү','ө']#ичке үндүлөр
wide_vowels = ['а','ы','о','у']#жоон үндүлөр
all_punctuation_marks = ['.',',','?','!','"',';',':','{','}','`',
                         '«', '»', '/', '(', ')', '#', '№', '$',
                         '^', '&', '*', '_', '-', '–', '+','=', '~', "|"]
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
faces = ['p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf']
all_faces = ['p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf', 'p3sg', 'p3pl']
possessiveness = ['px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf']
plural = 'pl'
ques = 'ques'
agent_noun = 'agnt'
p2sgf_str = 'p2sgf'
poss_general = 'xp'
for_poss = ['p1pl','px2pl', 'p2sgf', 'px2sgf']
all_sg = ['sg','p3sg']
gerunds = ['ger','ger_pres','ger_fut','fut_opt']
chakchyl = ['gna_perf','gna_purp','gna_cnd','gna_irre','advv_cont']
atoochtuk = ['gpr_aor_neg','gpr','gpr_impf','gpr_pres']
verb_pres = ['да','до','дө']
inf1_2 = ['ger']
for_pst_evid = ['тыр','тир','тур','түр']
gna_perf = 'gna_perf'
for_pst_evid2 = ['ып','ип','уп','үп','п']
negative_ending_verb = ['ба', 'бе', 'бө', 'бо', 'па', 'пе', 'пө', 'по']
imp_pl_1 = ['кы','ки','ку','кү','гы','ги','гу','гү']
imp_pl_2 = ['ла','ле','ло','лө']
fut_indf_endings = ['а','е','о','ө']
two_sgf = 'p2sgf'
two_sgf_ending = ['ыңыз','иңиз','уңуз','үңүз']
imp_p2sgf = ['ңыз','ңиз','ңуз','ңүз']
ger_pres = ['ыш','иш','уш','үш','ш']
fut_indf_1pl = ['лы','ли','лу','лү']
hor_pl2 = ['лык','лик','лук','лүк']
hor_pl3 = ['алы','ели','олу','өлү','йлы','йли','йлу','йлү']
hor_pl4 = ['алык','елик','олук','өлүк','йлык','йлик','йлук','йлүк']
neg_str = 'neg'
fut_indf_str = 'fut_indf'
deside2 = ['макчы','мекчи','мокчу','мөкчү']
inf_5_1sg = ['гым','гим','гум','гүм','кым','ким','кум','күм']
inf_5_2sg = ['гың','гиң','гуң','гүң','кың','киң','куң','күң']
past_def = ['ты','ти','ту','тү','ды','ди','ду','дү']
neg_pres2 = ['оодо','өөдө']
neg_pre1 = ['б','п']
fut_aor = ['ар','ер','ор','өр']
fut_indf_neg = 'fut_indf_neg'
advv_int1 = ['ны','ни','ну','нү']
advv_int2 = ['га','ге','го','гө', 'ка','ке','ко','кө']
gna_cnd = ['майынча','мейинче','мойунча','мөйүнчө']
num_appr1 = 'num_appr1'
advv_suc1 = ['кыча','киче','куча','күчө','гыча','гиче','гуча','гүчө']
advv_suc2 = ['ганча','генче','гончо','гөнчө','канча','кенче','кончо','көнчө']
hor_sg_str = 'fut_indf'
advv_neg2 = ['майын','мейин','мойун','мөйүн']
past_iter = 'past_iter'
gpr_1 = ['оочу','уучу','өөчү','үүчү']
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
shortcut_ending_poss = ['м','ң']
shortcut_ending_with_1_sg = ['ам','ем','ом','өм']
shortcut_ending_with_3_sg = ['ат','ет','от','өт']
fut_def_faces = ['та','те','то','тө','да','де','до','дө']
dat = 'dat'
pst_iter_1sg = ['чум','чүм']
pst_iter_2sg = ['чуң','чүң']
pst_iter_1pl = ['чук','чүк']
imp_together_tags = ['v','ques','neg','act','imp', 'iv', 'tv']
gerunds_together_tags = ['v','nom','gen','dat','acc','loc','abl', 'sg','pl','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl','px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
                  'ques','neg','xp','imp','act', 'iv', 'tv']
pcp_together_tags = ['v','pl','imp','act', 'nom','gen','dat','acc','loc','abl', 'sg','pl','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl','px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
                  'ques','neg','xp', 'iv', 'tv']
advv_together_tags = ['v','imp','act', 'iv', 'tv']
mood_together_tags = ['v','act','imp','neg','ques','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl', 'iv', 'tv']
prec_1_together_tags = ['v','act','imp','neg', 'iv', 'tv']
comp_together_tags = ['adj','pst','attr']

opt_together_tags = ['v','iv','tv','act','imp','neg','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf', 'p3sg','p3pl','px3sg']
advv_tags = ['gna_perf', 'advv_cont','gna_purp', 'gna_cnd','gna_irre']
gerunds_tags = ['ger','ger_pres','ger_fut','fut_opt']
pcp_tags = ['gpr','gpr_impf','gpr_aor_neg','gpr_pres']
verb_mood = ['pres','past_def','past_indf','past_evid','past_iter','fut_def', 'fut_aor','fut_indf_neg','cnd','fut_indf']
imp_tags = ['imp']
tags_with_noun = ['n','nom','gen','dat','acc','loc','abl', 'sg','pl','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl','px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
                  'ques','agnt','neg','xp']
tags_with_numeral = ['num','num_card','nom','gen','dat','acc','loc','abl', 'sg','pl','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl','px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
                  'ques','neg','xp']
numeral_tags = ['num_card','num_ord','num_coll','num_top','num_appr1','num_appr2','num_appr3']
adj_ending_tags = ['comp']
adj_tags = ['pst']
tags_with_adj = ['adj','pst','nom','gen','dat','acc','loc','abl', 'sg','pl','p1sg', 'p2sg', 'p2sgf', 'p1pl', 'p2pl', 'p2plf',
                  'p3sg','p3pl','px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
                  'ques','neg','xp', 'attr']
fut_def_special = ['йм']
fut_def_special_negative = ['бай', 'бей', 'бөй', 'бой', 'пай', 'пей', 'пөй', 'пой']
cond_1sg = ['сам','сем','сом','сөм']
cond_2sg = ['саң','сең','соң','сөң']
cond_1pl = ['сак','сек','сок','сөк']
optative_mood_1sg_1pl = ['fut_indf','fut_indf']
hor_together_tags = ['v','ques','neg']
inf_1_inf_2_with_shortcut_faces = ['оом','уум','өөм','үүм', 'ооң','ууң','өөң','үүң']
inf_1_with_shortcut_1sg = ['оом', 'өөм']
inf_2_with_shortcut_1sg = ['уум', 'үүм']
inf_1_with_shortcut_2sg = ['ооң', 'өөң']
inf_2_with_shortcut_2sg = ['ууң', 'үүң']
poss_1sg_2sg = ['px1sg', 'px2sg']
advv_acc_latest_letter = 'п'
plural_ending = ['дар', 'дер', 'дор', 'дөр', 'тар', 'тер', 'тор', 'төр', 'лар', 'лер', 'лор', 'лөр']
pcp_pr_1 = ['уучу','оочу','үүчү','өөчү']
past_indf = 'past_indf'
change_tags_without_faces = ['pl', 'px1sg', 'px2sg', 'px2sgf', 'px3sg', 'px1pl', 'px2pl', 'px2plf',
               'gen','dat','acc','loc','abl', 'xp']
gpr_2 = ['гон', 'гөн', 'ген', 'ган','кон', 'көн', 'кен', 'кан']
fut_indf_neg_str = 'fut_indf_neg'
inf_1_ending = ['оо','өө']
inf_2_ending = ['уу','үү']
fut_aor_str = 'fut_aor'
fut_opt = ['кы','ки','ку','кү','гы','ги','гу','гү']
pst_iter_str = 'past_iter'
prec_1_str = 'prec_1'
num_ord = ['ынчы', 'инчи', 'үнчү', 'унчу']
num_ord_short = ['нчы', 'нчи', 'нчү', 'нчу']
num_word_special = ['үчүнчү', 'алтынчы','кыркча','кырктай','кырктан','кырктаган','бирөө','экөө','үчөө','төртөө',
                    'бешөө','алтоо','жетөө','сегизөө']
adj_word_special = ['жакшыраак']
part_of_speech_tags = ['post']
abl_str = 'abl'
num_appr3 = ['догон', 'дөгөн', 'деген', 'даган',
    'тогон', 'төгөн', 'теген', 'таган']
comp_str = 'comp'
POS_without_ending_tags = ['ij','ideo','conj','post','mod','part']
shortcut_poss_3sg_ending = ['ы','и','у','ү']
poss_1sg_2sg_endings = ['ым','им','ум','үм','ың','иң','уң','үң']
poss_1sg_endings = ['ым','им','ум','үм']
poss_2sg_endings = ['ың','иң','уң','үң']
px2sgf_endings = ['ңыз','ңиз','ңуз','ңүз']
px1pl_endings = ['быз','биз','буз','бүз']
px2pl_endings = ['ңар','ңер','ңор','ңөр']
comp_endings = ['ы','и','у','ү']
verb_default_tags = ['v', 'act', 'iv', 'tv', 'imp', 'caus','coop', 'ref', 'pass']