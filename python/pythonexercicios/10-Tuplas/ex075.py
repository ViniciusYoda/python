num = (int(input('Digite um número')), int(input('Digite um número')), int(input('Digite um número')), int(input('Digite um número')))
print(f'Você digitou os valores {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3) + 1}º posição')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')