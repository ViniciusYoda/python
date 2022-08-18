def media_final():
    media = float(input('Qual é a sua média final? '))
    return media

def nota(media):
    if media <= 4.9:
        msg = 'D'
    elif media <= 6.9:
        msg = 'C'
    elif media <= 8.9:
        msg = 'B'
    elif media <= 10:
        msg = 'A'
    return msg

def principal():
    media = media_final()
    print(nota(media))

principal()
