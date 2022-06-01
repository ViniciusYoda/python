salarios = []
soma = 0
for _ in range(4):
    salario = float(input('Salário: R$'))
    soma += salario
    salarios.append(salario)
media = soma / 4
for salario in salarios:
    if salario < media:
        print(f'Abaixo da média: R$ {salario:.2f}')