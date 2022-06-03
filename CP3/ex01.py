print("Qual o melhor Sistema Operacional para uso em servidores?")
print('''1 - Windows Server 2- Unix 3-Linux 4- Netware, 5- Mac OS, 6- Outro''')

opcoes = ['falta de toner', 'necessita de limpeza', 'troca do cabo', '',]
sistemas = [0] * 4

while True:
    #VAlidar a entrada do usuário
    while True:
        opcao = int(input('Digite a opção: '))
        if opcao < 0 or opcao > 6:
            print('Opçao inválida')
        else:
            break
    if opcao == 0:
        break
    elif opcao == 1:
        sistemas[0] += 1
    elif opcao == 2:
        sistemas[1] += 1
    elif opcao == 3:
        sistemas[2] += 1
    elif opcao == 4:
        sistemas[3] += 1
    
#sistemas[opcao-1] += 1

print('Sistema Operacional     Votos %')
print('-----------------------------------') 
cont = 0
melhor = 0
melhorSis = ''
perc = 0
for s in sistemas:
    print(f'{opcoes[cont]} {s} {(s*100)/sum(sistemas)}')
    if s > melhor:
        melhor = s
        melhorSis = opcoes[cont]
        perc = (s * 100) / sum(sistemas)
    cont += 1

print('----------------------------')
print(f'Total: {sum(sistemas)}')
print(f'O sistemas operacional mais votado foi {melhorSis} com {melhor} {perc}')



