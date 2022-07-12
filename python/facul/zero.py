#Crie um programa que leia cinco nomes e exiba a quantidade de nomes que começam com vogal

nomes = [] #criando uma lista vazia
for _ in range(5): #iteração com números
    nome = input('Nome: ')
    nomes.append(nome) #append - adiciona um item no fim da lista

qtd = 0
for nome in nomes: #iteração com itens da lista
    if(nome[0]=='A' or nome[0]=='E' or nome[0]=='I' or nome[0]=='O' or nome[0]=='U' ):
        qtd += 1
        
print(f'{qtd} dos nomes começam com vogal')