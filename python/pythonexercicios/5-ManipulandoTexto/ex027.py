n = str(input('Digite seu nome completo: ')).upper().strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nomé é {}'.format(nome[len(nome)-1]))