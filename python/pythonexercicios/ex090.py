aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f"Média do {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média é {aluno["media"]}')
print(f'A situação dele é de {aluno["situação"]}')

for k, v in aluno.items():
    print(f'{k}: {v}')