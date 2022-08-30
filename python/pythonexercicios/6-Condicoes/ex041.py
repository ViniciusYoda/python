from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <=9:
    print('O atleta está na categoria Mirim')
elif idade <=14:
    print('O atleta está na categoria Infantil')
elif idade <=19:
    print('O atleta está na categoria Júnior')
elif idade <=25:
    print('O atleta está na categoria Sénior')
else:
    print('O atleta está na categoria Master')
