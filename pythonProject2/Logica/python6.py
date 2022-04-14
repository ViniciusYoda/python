nota1 = int(input('Nota1: '))
nota2 = int(input('Nota2: '))
nota3 = int(input('Nota3: '))
media = (nota1 + nota2 + nota3)/3
pres = int(input('Total de faltas: '))
final = (media + pres)/2
if final  >= 6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado, necessario fazer um novo exame')
exame = int(input('Nota do seu exame: '))
if exame >= 6:
    print('Aluno aprovado no exame')
else:
    print('Aluno reprovado, sem mais chances')