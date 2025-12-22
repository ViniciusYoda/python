print('Olá, Mundo!')
print(7 + 4)
print('7' + '4')
print('Olá', 5)
print('Olá', 5, sep=' - ')
print('Olá', 5, end=' - ')
print('Tudo bem?')
# \n - quebra de linha
# \t - tabulação
# \ - caractere de escape
# \ - caractere de continuação
nome = 'Alan'
idade = 25
peso = 75.8
print(nome, idade, peso)
print(nome, idade, peso, sep=', ')
print(nome, idade, peso, sep=', ', end='!')
print()
print(f'{nome} tem {idade} anos e pesa {peso}Kg.')
print(f'{nome} tem {idade} anos e pesa {peso:.2f}Kg.')
nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual é o seu peso? ')
print(nome, idade, peso)
print(f'{nome} tem {idade} anos e pesa {peso}Kg.')