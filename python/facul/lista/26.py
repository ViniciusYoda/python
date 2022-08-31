#Crie um programa que leia cinco nomes e exiba a quantidade de nomes que começam com vogal.
nomes = []
for _ in range(5):
    nomes.append(input('Nome: '))
qtd = 0
for nome in nomes:
    if (nome[0]=='A' or nome[0]=='E' or nome[0]=="I" or nome[0]=="O" or nome[0]=="U"):
        qtd += 1
print(f'{qtd} dos nomes começam com vogal')