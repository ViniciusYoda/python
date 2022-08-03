lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite o {i} valor da lista: ')))
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

# variaveis de controle (flags)
x = 0 #percorrer a lista
achou_n1 = False #variavel (flag) booleana
achou_n2 = False #variavel (flag) booleana
primeiro = 0 #controla que apareceu primeiro na lista

while x < len(lista):
    if lista[x] == n1:
        achou_n1 = True
        if not achou_n2: # if achou_n2 == False
            primeiro = 1
    if lista[x] == n2:
        achou_n2 = True
        if not achou_n1:
            primeiro = 2
    x+=1

if achou_n1 == True:
    print(f'O número {n1} foi encontrado')
else:
    print(f'O número {n1} não foi encontrado')

if achou_n2 == True:
    print(f'O número {n2} foi encontrado')
else:
    print(f'O número {n2} não foi encontrado')

if primeiro == 1:
    print(f'O número {n1} foi encontrado antes de {n2}')
elif primeiro == 2:
    print(f'O número {n2} foi encontrado antes de {n1}')
    