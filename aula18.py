teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galerea = [['João', 19], ['Maria', 25], ['Pedro', 32]]  
print(galerea)
print(galerea[0][0])
print(galerea[1][1])
print(galerea[2][0])
for p in galerea:
    print(f'{p[0]} tem {p[1]} anos de idade.')

pasta = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pasta.append(dado[:])
    dado.clear()
print(pasta)
for p in pasta:
    print(f'{p[0]} tem {p[1]} anos de idade.')

for m in pasta:
    if m[1] >= 18:
        print(f'{m[0]} é maior de idade')	
    else:
        print(f'{m[0]} é menor de idade')
print(f'Você tem {len(pasta)} pessoas cadastradas.')
for i, v in enumerate(pasta):
    print(f'{i}: {v}')
