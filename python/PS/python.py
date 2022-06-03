print('|Falta de Toner|', '|Necessita de limpeza|', '|Troca do cabo ou conector|', '|Quebrado ou inutilizado|')
problema = [] 
cont = []
for c in range(4):
    print('Digite o problema')
    problema.append(input('Digite o problema: '))
    cont.append(int(input('Digite o número de problema: ')))

print('Resultado')
maiorOcorrencia = 0
cont = 0
prob = ''
for c in enumerate(problema):
    print(f'{problema} - {cont} - {cont / 10 * 100}%')
    


