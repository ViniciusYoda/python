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