from random import randint
print('-=' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 30)
v = 0
while True:
    c = randint(0, 10)
    n = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    s = c + n
    print(f'Você jogou {n} e o computador {c}. Total de {s} ', end='')
    print('DEU PAR' if s % 2 == 0 else 'DEU ÍMPAR')
    if pi == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif pi == 'I':
        if s % 2 != 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')