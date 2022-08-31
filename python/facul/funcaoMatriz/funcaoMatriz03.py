def coletar_notas():
    notas = []
    for i in range(3):
        nota = float(input(f'Nota{i+1}: '))
        notas.append(nota)
    return notas

def preenche_turma(qtde_alunos):
    turma = []
    for i in range(qtde_alunos):
        print(f'{i+1}° aluno: ')
        aluno = coletar_notas()
        turma.append(aluno)
    return turma

def calcula_media(aluno):
    soma = 0
    for nota in aluno:
        soma += nota
    return soma / len(aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcula_media(aluno)
        print(f'notas: {aluno} | média: {media:.2f}')

def principal():
    qtde_alunos = int(input('Total de alunos: '))
    turma = preenche_turma(qtde_alunos)
    resumo_turma(turma)

principal()