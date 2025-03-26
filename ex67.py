print('-' * 30)
while True:
    n = int(input('Quer ver a tabuada de qual valor?: Digite um número negativo para parar '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('Programa encerrado.')