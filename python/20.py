salarios = [0, 0, 0, 0]
soma = 0
salarios[0] = float(input('Salário: R$'))
soma += salarios[0]
salarios[1] = float(input('Salário: R$'))
soma += salarios[1]
salarios[2] = float(input('Salário: R$'))
soma += salarios[2]
salarios[3] = float(input('Salário: R$'))
soma += salarios[3]
media = soma / 4
if salarios[0] < media:
    print(f'Abaixo da média: R$ {salarios[0]:.2f}')
if salarios[1] < media:
    print(f'Abaixo da média: R$ {salarios[1]:.2f}')
if salarios[2] < media:
    print(f'Abaixo da média: R$ {salarios[2]:.2f}')
if salarios[3] < media:
    print(f'Abaixo da média: R$ {salarios[3]:.2f}')