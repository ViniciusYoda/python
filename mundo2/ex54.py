from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
print('Fim')
