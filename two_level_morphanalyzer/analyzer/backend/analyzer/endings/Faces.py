def get_info_faces(ending):
    if ending in face_1st_sg:
        return "p1sg"
    elif ending in face_1st_pl:
        return "p1pl"
    elif ending in face_2st_sg or ending in face_2st_sg_politely:
        return "p2sg"
    elif ending in face_2st_pl or ending in face_2st_pl_politely:
        return "p2pl"
    else:
        return 'none'

face_1st_sg = {
    'мын', 'мин', 'мун', 'мүн', 'м'
}
face_2st_sg = {
    'сың', 'сиң', 'суң', 'сүң', 'ң'
}
face_2st_sg_politely = {
    'сыз', 'сиз', 'суз', 'сүз', 'ңыз'
}
face_1st_pl = {
    'быз', 'биз', 'буз', 'бүз', 'к',
    'пыз', 'пиз', 'пуз', 'пүз'
}
face_2st_pl = {
    'сыңар', 'сиңер', 'суңар', 'сүңөр', 'ңар'
}
face_2st_pl_politely = {
    'сыздар', 'сиздер', 'суздар', 'сүздөр', 'ңыздар'
}