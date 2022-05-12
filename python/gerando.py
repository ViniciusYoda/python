salario = [0, 0, 0, 0]
soma = 0

salario[0] = float(input('Salário: '))

soma+= salario[0]

salario[1] = float(input('Salário: '))
soma+= salario[1]

salario[2] = float(input('Salário: '))
soma+= salario[2]

salario[3] = float(input('Salário: '))
soma+= salario[3]

media = soma/4

if salario[0] < media:
    print(f'abaixo da média: R$ {salario[0]:.2f}')

if salario[1] < media:
    print(f'abaixo da média: R$ {salario[1]:.2f}')

if salario[2] < media:
    print(f'abaixo da média: R$ {salario[2]:.2f}')

if salario[3] < media:
    print(f'abaixo da média: R$ {salario[3]:.2f}')

print(f'A média é de: {media:.2f} ')