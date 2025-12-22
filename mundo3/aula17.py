num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.remove(2)
print(num)
num.pop(2)
print(num)
num.pop()
print(num)
num.clear()
print(num)
num = [2, 5, 9, 1]
print(num)

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
valores.sort(reverse=True)
print(valores)
print(f'Os valores em ordem decrescente são {valores}')
print(f'O maior valor é {max(valores)}')
print(f'O menor valor é {min(valores)}')
print(f'A soma dos valores é {sum(valores)}')
print(f'A média dos valores é {sum(valores)/len(valores)}')
print(f'A quantidade de valores é {len(valores)}')
print(f'O primeiro valor é {valores[0]}')
print(f'O último valor é {valores[-1]}')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

a = [2, 3, 4, 5]
b = a[:]
b[2] = 8

print(f'A: {a}')
print(f'B: {b}')
print(f'Endereço de A: {id(a)}')
print(f'Endereço de B: {id(b)}')
print(f'Endereço de A[0]: {id(a[0])}')
print(f'Endereço de B[0]: {id(b[0])}')
