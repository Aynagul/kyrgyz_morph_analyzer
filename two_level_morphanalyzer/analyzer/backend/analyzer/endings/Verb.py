'''
elif (symbol := Noun.get_info_noun_ending_from_verb(ending)) != 'none':
                    new_list, new_word = block_of_verb.noun_ending_from_verb(self, index, new_list, symbol,
                                                                                     str_ending)
                    if self.find_root_from_the_end(new_word):
                        break
                    else:
                        new_list.reverse()
                        continue

'''
def get_indo_verb_ideophone_to_verb(ending):
    if ending in verb_ideophone_to_verb:
        return 'v'
    else:
        return 'none'
def get_info_verb_verb_to_verb(ending):
    if ending in verb_verb_to_verb_more_used:
        return 'v'
    elif ending in verb_verb_to_verb_less_used or ending in verb_verb_to_verb_useless:
        return 'v'
    else:
        return 'none'
def get_info_verb_other_to_verb(ending):
    if ending in verb_other_to_verb_more_used:
        return 'v'
    elif ending in verb_other_to_verb_less_used or ending in verb_other_to_verb_useless:
        return 'v'
    else:
        return 'none'
def get_voice(ending):
    if ending in v_voice_reflexive:
        return 'ref'
    elif ending in v_voice_cooperative:
        return 'coop'
    elif ending in v_voice_passive:
        return 'pass'
    elif ending in v_voice_causative:
        return 'caus'
    else:
        return 'none'
def get_mood(ending):
    if ending in v_tense_present:
        return 'ind_pres'
    elif ending in v_tense_past:
        return 'ind_past'
    elif ending in v_tense_future:
        return 'ind_fut'
    elif ending in v_mood_imperative:
        return 'imp'
    elif ending in v_mood_conditional:
        return 'cnd'
    elif ending in v_mood_subjunctive:
        return 'niet'
    elif ending in v_mood_imperfect:
        return 'opt'
    else:
        return 'none'
#этиштин мамилелери
v_voice_active = {     # негизги мамиле
}

v_voice_reflexive = {     #оздук мамиле
    'ын', 'ан', 'ун', 'үн', 'ың',   #эгин жүгүнөт
    'ыл', 'ол', 'өл', 'ул', 'үл',   #күн бүркөлдү
    'ылда', 'улда'     #жыркылда


}
v_voice_cooperative = {   #кош мамиле
    'ыш', 'иш',     #кылышты
    'аш', 'еш', 'уш', 'үш' #иштештик
}
v_voice_passive = {   #туюк мамиле
    'ыл', 'ул', 'үл', 'ил',  #жабыл
}
v_voice_passive_exception = {   #туюк мамиле исключение (л тыбыш менен буткон этиштер)
    'ын', 'ин', 'ун', 'үн', 'ың'    #тилин
}
v_voice_causative = {     #аркылуу мамиле
    'дыр', 'тыр', 'дур', 'дүр', 'тур', 'түр', 'дир', 'тир', #бастыр
    'кар', 'гар', 'көр', 'тар', #башкар
    'каз', 'коз', 'көз', 'гөз', #көргөз
    'кыз', 'киз', 'гуз', 'гиз', 'гыз', 'из', 'ыз', 'гүз','куз','күз', #тургуз
    'кыр', 'кир', #жаткыр
    'ыр', 'ир', 'ур', 'үр', #учур
    'сөт', #көрсөт
    'т' #байкат
}

#этиштин ынгайлары
v_mood_indicative_present = {   #Баяндагыч ыңгай учур чакта
}
v_mood_indicative_past = {   #Баяндагыч ыңгай өткөн чакта

}
v_mood_indicative_future = {   #Баяндагыч ыңгай келер чакта

}

v_mood_imperative = {   #буйрук ыңгай

    'гын','гының','гун','гүн', 'гунуң','гүнүң', 'гин', 'гиниң',     #жүргүн - p2sg
    'кын','кының','кун','күн', 'кунуң','күнүң', 'кин', 'киниң',
    'ыңыз', 'иңиз', 'үңүз', 'уңуз', #келиңиз - p2sg politely
    'гыла','гиле','гула','гүлө',    #тургула - p2pl
    'кыла','киле','кула','күлө',
    'сын','син','сун','сүн',     #уксун - p3
    'чы', 'чи', 'чу', 'чү'       #кетчи
}
v_mood_conditional = {   #шарттуу ыңгай
    'са','се','со','сө'     #келсе
}
v_mood_imperfect = {   #каалоо-тилек ыңгай - v_fut
    'гай','гей'  #баргаймын
    'алы', 'ели',  #баралы - p1pl
    'айын', 'ейин',     #телейин
}
v_mood_subjunctive = {   #максат-ниет ыңгай - v_fut
    'мак','мек','макчы','мекчи'     #бармакчы
}

#этиштин чактары
v_tense_present = {   #учур чак
    'ууда','үүдө',  #айдалууда
    'дыр'      #арбындыр
}
v_tense_past = {   #өткөн чак
    'ыптыр','иптир','уптур','үптүр','аптыр',    #жамандаптыр
    'ып','ип','уп','үп','ап'    #келипмин 
    'уучу','үүчү', 'оочу',
    'чу', 'чү', 'ышчу',    #барышчу
    'ды','ди','ду','дү',
    'ты','ти','ту','тү',#келди
    'ган','ген', 'гон','гөн',   #калган
    'кан','кен', 'кон','кен'
}
v_tense_future = {   #келер чак
    'а','е','й',    #окуймун, барат
    'ар', 'ор'  #айтар
    'бас','бес','бос','бөс',    #өлбөс
    'пас','пес','пос','пөс'
}

#этиштин өзгөчө формалары
#чакчыл
def get_chakchyl(ending):
    if ending in v_chakchyl_advv_acc:
        return 'advv_acc'
    else:
        return 'none'
v_chakchyl_advv_acc = {
    'ып', 'ип','уп','үп', 'п', 'ап'  #
}
v_chakchyl_advv_int = {
    'ганы', 'гени', 'гону', 'гөнү',
    'каны', 'кени', 'кону', 'көнү'
}
v_chakchyl_advv_neg = {
    'майынча', 'мейинче', 'мойунча', 'мөйүнчө',
    'майын', 'мейин', 'мойун', 'мөйүн'
}
v_chakchyl_advv_suc= {
    'гыча', 'гиче', 'гуча', 'гүчө',
    'кыча', 'киче', 'куча', 'күчө',
    'ганча', 'генче', 'гончо', 'гөнчө',
    'канча', 'кенче', 'кончо', 'көнчө'
}
v_chakchyl_advv_cont = {   #чакчыл
    'а', 'е', 'ы', 'о', 'ө',
    'й'
}

#атоочтук
def get_atoochtuk(ending):
    if ending in v_atoochtuk_pcp_ps:
        return 'pcp_ps'
    elif ending in v_atoochtuk_pcp_fut_neg:
        return 'pcp_fut_neg'
    elif ending in v_atoochtuk_pcp_fut_def:
        return 'gpr_impf'
    elif ending in v_atoochtuk_gpr_pres:
        return 'gpr_pres'
    elif ending in v_atoochtuk_pcp_pr:
        return 'pcp_pr'
    else:
        return 'none'
v_atoochtuk_pcp_ps = {
    'ган','ген', 'гон', 'гөн',   #эгилген
    'кан','кен', 'кон', 'көн'

}
v_atoochtuk_pcp_fut_neg = {
    'бас','бес','бос','бөс',    #өлбөс-
    'пас','пес','пос','пөс',
}
v_atoochtuk_pcp_fut_def = {
    'ар','өр','ор','ер',   #агар-

    'гыдай','гидей','гудай','гүдөй',     #жаагыдай
    'чудай','чидей','чыдай','чүдөй',     #айтчудай
    'гандай','гендей','гондой','гөндөй',     #шыбырагандай
}
v_atoochtuk_gpr_pres = {
    'гыс','гус','гис','гүс'     #түгөнгүс
    'мыш',                #мыш
    #аган
    'максан','мексен','мөксөн','моксон'     #билмексен
}
v_atoochtuk_pcp_pr = {
    'уучу','үүчү', 'оочу'   #куйкалоочу
}

#кыймыл атооч
def get_gerund(ending):
    if ending in v_gerund_inf_1:
        return 'inf_1'
    elif ending in v_gerund_inf_2:
        return 'inf_2'
    elif ending in v_gerund_inf_3:
        return 'inf_3'
    elif ending in v_gerund_inf_4:
        return 'inf_4'
    elif ending in v_gerund_inf_5:
        return 'inf_5'
    else:
        return 'none'
'''v_gerund_ger_perf = {
    '','','',''      #
}'''
v_gerund_inf_4 = {
    'мак','мек', 'мок','мөк',     #отурмак
    'май','мей','мөй','мой'       #бермей
}
v_gerund_inf_3 = {
    'аш','ыш','иш','уш','үш', 'өш'      #караш-
}
v_gerund_inf_5 = {
    'гы','ги','гу','гү',
    'кы','ки','ку','кү'#
}
v_gerund_inf_1= {
    'оо', 'өө'    #уруу- жана толтура
}
v_gerund_inf_2= {
    'уу', 'үү'
}

#how verb is made
verb_other_to_verb_more_used = {
    'а','о','ө','е',    #сана-
    'ай','ой','өй','ей',    #азай-
    'ар','өр','ир','ор','ер',   #агар-
    'ла','да','де','до','дө','та','те','то','тө','ле','ло','лө',#дарыла-
    'лан','лон','лөн','дан','ден', 'тан','тен',#тынчтан-
    "лаш", "леш", "лош", "лөш", #акылдаш-
    "даш", "деш", "дош", "дөш",
    "таш", "теш", "тош", "төш",
    'сыра','сире','сура','сүрө',#алсыра-
    'ык', 'ик', 'ук', 'үк',     #кечик-
    'ырка','урка','үркө','арка','ирке'  #жабырка-
}
verb_other_to_verb_less_used = {
    'ал','ыл','ол','ул','ил',   #тирил
    'ке',   #теске-
    'сы','си','су','сү',    #кыйынсы-
    'сын','син','сун','сүн',    #тыңсын-
    'шы','шу','шү','ши',    #быкшы-
    'ы','у','и'    #быйы-
}
verb_other_to_verb_useless = {
    'ан',   #оозан-
    'ыт','от','өт', #жогот-
    'бар','быр',    #албыр-
    'лук','дык',    #ардык- ,соолук-
    'ра','ро',      #куура-
    #'са','сө','се', #сууса-
    'сун',      #бойсун-
    'ча',       #кырча-
    'чый','чий','чуй','чүй',    #тикчий-
    'чыла','чиле','чүлө',   #кедейчиле
    'ша',       #какша-
    'шырай','ширей' #акшырай-
}

verb_verb_to_verb_more_used = {
    'гансы','генси','гөнсү','гонсу',    #ачкансы-
    'кансы','кенси','көнсү','консу',
    'гыла','гула','гүлө','гиле',    #кескиле-
    'кыла','кула','күлө','киле',
    'ла','ло','лө',     #сыйпала-
    "лык", "лик", "лук", "лүк",     #буулук-
    "тык", "тик", "тук", "түк",
    "дык", "дик", "дук", "дүк",
    'мала','меле','моло','мөлө',    #бурмала-
    'ын','ин','ун','үн',        #сүйүн-
    'алан','елен','олон','өлөн'     #созолон-
}
verb_verb_to_verb_less_used = {
    'а','ө',    #кура-
    'ала','еле',    #тебеле-
    'ар','ер','ор','өр',    #чыгар-
    'тар','тор','төр',      #кыстар-
    'жы','жу',      #чоюлжу-
    'ка','ке','кө', #ийке-
    'ра',       #кыйра-
    'шта',      #ыргышта-
    'ык','үк','ук'  #канык-
}
verb_verb_to_verb_useless = {
    'ай','ей',  #кечирей-
    'гала','голо',  #тайгала-
    'к',        #тынык-
    'ман','мен',    #иймен-
    'маш','мыш',    #таймаш-
    #'са','се','сө', #өксө-
    'чы',       #чапчы-
    'чыла','чула','чоло',   #барчыла-
    'шыр'       #жапшыр-
}

verb_ideophone_to_verb = {
    'ай','ой','ей','ый','өй',   #торсой-
    'ый','ий','уй','үй',        #балкый-
    'ылда','улда','үлдө',       #арсылда-
    'ыра','ире',    #жаркыра-
    'а','е',        #чыркыра-
    'шы','шый'      #быкшы- ,быкшый-
}
