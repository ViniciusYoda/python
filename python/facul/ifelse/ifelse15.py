nota1 = int(input('Escreva sua primeira nota: '))
nota2 = int(input('Escreva sua segunda nota: '))
nota3 = int(input('Escreva sua terceira nota: '))
media = (nota1 + nota2 + nota3)/3
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
pres = int(input('Escreva seu total de faltas: '))
if pres <=18:
    print('Aluno  aprovado')