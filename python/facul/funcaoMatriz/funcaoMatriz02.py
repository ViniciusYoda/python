'''aluno_0_0, aluno_0_1, aluno_0_2 = 5.5, 7.0, 8.7
aluno_1_0, aluno_1_1, aluno_1_2 = 8.5, 6.0, 9.2
aluno_2_0, aluno_2_1, aluno_2_2 = 7.8, 8.3, 8.5
aluno_3_0, aluno_3_1, aluno_3_2 = 0.0, 9.9, 9.1'''

aluno_0 = [5.5, 7.0, 8.7]
aluno_1 = [8.5, 6.0, 9.2]
aluno_2 = [7.8, 8.3, 8.5]
aluno_3 = [0.0, 9.9, 9.1]


alunos = [aluno_0, aluno_1, aluno_2, aluno_3]

def calcular_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

#programa principal
print('Aluno 0')
media = calcular_media(aluno_0)
print(f'Média: {media:.2f}')
print('Aluno 1')
media = calcular_media(aluno_1)
print(f'Média: {media:.2f}')