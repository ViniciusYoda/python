num = [[],[]]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores')
num[0].sort()
print(f'Os valores pares são {num[0]}')
num[1].sort()
print(f'Os valores impares são {num[1]}')