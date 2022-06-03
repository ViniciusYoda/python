print('Tipo de defeito do equipamento')
print(''' 1- Falta de toner
2- Necessita de limpeza
3- Troca de cabo ou conector
4- Quebrada ou inutilizada''')

opcoes = ["1- Falta de toner ", "2- Necessita de limpeza","3- Troca de cabo ou conector", "4- Quebrada ou inutilizada"]
sistemas = [0,0,0,0]

while True:
    while True:
        opcao = int(input('Digite a opção: '))
        if opcao < 0 or opcao > 4:
            print('opcao invalida')
        else:
            break
    if opcao == 0:
        break
    sistemas[opcao-1] += 1

print('Situação                                 Quantidade              Percentual')
print('------------------------------------------------------------------------------')

cont = 0
maior =0
maisVot= ''
perc = 0
for s in sistemas:
    print(f'{opcoes[cont]} - {s} - {(s * 100)/sum(sistemas):.2f}%')
    if s > maior:
        maior = s
        maiorVot = opcoes[cont]
        perc = (s * 100)/sum(sistemas)
    cont += 1

print('-------------------------------------------------------------------------------')
print(f'Total de impressoras: {sum(sistemas)}')
print(f'Defeito mais votado foi: {maiorVot}')
print(f'Quantidade de votos foi de: {maior} votos')
print(f'Porcentagem: {perc:.2f}% dos votos')

    