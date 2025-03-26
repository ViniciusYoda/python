print('-=' * 30)
print('CADASTRE UMA PESSOA')
print('-=' * 30)
m = f = h = 0
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if i >= 18:
        m += 1
    if s == 'F':
        f += 1
    if s == 'M':
        h += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {m}')
print(f'Ao todo temos {h} homens cadastrados.')
print(f'Ao todo temos {f} mulheres com menos de 20 anos.')
print('Fim do programa')