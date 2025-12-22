jogadores = []

while True:
    jogador = {}
    partidas = []

    jogador['nome'] = input("Nome do jogador: ")
    total_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for i in range(total_partidas):
        gols = int(input(f"Quantos gols na partida {i + 1}? "))
        partidas.append(gols)

    jogador['gols'] = partidas
    jogador['total'] = sum(partidas)

    jogadores.append(jogador)

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

print("\n{:<4} {:<15} {:<15} {:<5}".format("ID", "Nome", "Gols", "Total"))
print("-" * 40)
for idx, jogador in enumerate(jogadores):
    print(f"{idx:<4} {jogador['nome']:<15} {str(jogador['gols']):<15} {jogador['total']:<5}")

while True:
    print("\nDigite o ID do jogador para ver os detalhes (-1 para sair):")
    opcao = int(input("ID: "))
    if opcao == -1:
        break
    if opcao >= len(jogadores) or opcao < -1:
        print("ID inválido! Tente novamente.")
    else:
        jogador = jogadores[opcao]
        print(f"\n-- LEVANTAMENTO DO JOGADOR {jogador['nome']}:")
        for i, gols in enumerate(jogador['gols']):
            print(f"  No jogo {i + 1} fez {gols} gols.")