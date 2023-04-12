def get_info_possessive(ending):
    if ending in posessiveness_1st_sg:
        return "poss_1sg"
    elif ending in posessiveness_1st_pl:
        return "poss_1pl"
    elif ending in posessiveness_2st_sg or ending in posessiveness_2st_sg_politely:
        return "poss_2sg"
    elif ending in posessiveness_2st_pl or ending in posessiveness_2st_pl_politely:
        return "poss_2pl"
    elif ending in posessiveness_general:
        return "xp"     #жалпы таандык
    elif ending in posessiveness_3st_sg:
        return "poss_3sg"  #sp means sg or pl
    else:
        return 'none'
posessiveness_1st_sg = {
    'ым', 'им', 'ум', 'үм', 'м'
}
posessiveness_2st_sg = {
    'ың', 'иң', 'уң', 'үң', 'ң'
}
posessiveness_2st_sg_politely = {
    'ыңыз', 'иңиз', 'уңуз', 'үңүз',
    'ңыз', 'ңиз', 'ңуз', 'ңүз'
}
posessiveness_for_poses_2st_pl_politely= {
    'ңыз', 'ңиз', 'ңуз', 'ңүз'
}
posessiveness_3st_sg = {
    'ы', 'и', 'у', 'ү',
    'сы', 'си', 'су', 'сү'
}
posessiveness_for_face_p2pl = {
    'сы', 'си', 'су', 'сү'
}
posessiveness_1st_pl = {
    'ыбыз', 'ибиз', 'убуз', 'үбүз',
    'быз', 'биз', 'буз', 'бүз'
}
posessiveness_2st_pl = {
    'ыңар', 'иңер', 'уңар', 'үңөр',
    'ңар', 'ңер', 'ңүр', 'ңөр'
}
posessiveness_2st_pl_politely = {#ыңыздар...
    'ыңыздар', 'иңиздер', 'уңуздар', 'үңүздөр',
    'ңыздар', 'ңиздер', 'ңүздөр', 'ңуздар'
}
posessiveness_3st_pl = { #like 3st_sg

}
posessiveness_general ={
    'ныкы', 'ники', 'нуку', 'нүкү',
    'дыкы', 'дики', 'дуку', 'дүкү',
    'тыкы', 'тики', 'туку', 'түкү'
}