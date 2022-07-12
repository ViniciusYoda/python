salario = [0, 0, 0, 0]
soma = 0
i = 0

while i < len(salario):
    salario[i] = float(input('Salário: '))
    soma+= salario[i]
    i+=1

    media = soma/len(salario)

    i=0
    while i < 4:
        if salario[i] < media:
            print(f'Abaixo da média: R$ {salario[i]:.2f}')
        i+=1


print(f'A média é de: {media:.2f} ')