from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nascem em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print("Você tem que se alistar imediatamente")
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta {} anos para alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistamwnto há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
