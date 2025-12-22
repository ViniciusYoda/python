aluno = {}

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input(f"Digite a média de {aluno['nome']}: "))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")