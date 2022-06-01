soma = 0
salario_0 = float(input('Salario: R$ '))
soma += salario_0
salario_1 = float(input('Salario: R$ '))
soma += salario_1
salario_2 = float(input('Salario: R$ '))
soma += salario_2
salario_3 = float(input('Salario: R$ '))
soma += salario_3
media = soma / 4
if salario_0 < media:
    print(f'Abaixo da média: RS {salario_0:.2f}')
if salario_1 < media:
    print(f'Abaixo da média: RS {salario_1:.2f}')
if salario_2 < media:
    print(f'Abaixo da média: RS {salario_2:.2f}')
if salario_3 < media:
    print(f'Abaixo da média: RS {salario_3:.2f}')