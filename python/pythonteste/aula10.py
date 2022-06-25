n1 = float(input('Digite a primeira nota '))
n2 = float(input('Digite a segunda nota '))
m = (n1+n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim!')
print('Parabens pelo notao' if m>=10 else 'Estude mais para chegar no 10')