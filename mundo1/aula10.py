nome = input('Qual é o seu nomme? ')
if nome == 'Vinícius':
    print('Que nome lindo você tem!')
else:
    print('Seu nome não é lindo')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('Sua média foi {:.1f}'.format(m))