nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno é {:.1f}'.format(media))
if 7 > media >= 5:
    print('O aluno está em recuperação')
elif media < 5:
    print('O aluno está reprovado')
else:
    print('Aluno aprovado')