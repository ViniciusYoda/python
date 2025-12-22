alunos = []

while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    
    alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("\nBoletim:")
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print("-" * 26)
for i, aluno in enumerate(alunos):
    print(f"{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}")

while True:
    opcao = int(input("\nMostrar notas de qual aluno? (999 para interromper): "))
    if opcao == 999:
        print("Finalizando...")
        break
    if 0 <= opcao < len(alunos):
        print(f"Notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
    else:
        print("Aluno não encontrado. Tente novamente.")