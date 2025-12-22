jogador = {}

jogador['nome'] = input("Nome do jogador: ")
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

gols = []
for i in range(partidas):
    gols.append(int(input(f"Quantos gols na partida {i + 1}? ")))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print("-=" * 30)
print(jogador)
print("-=" * 30)

for chave, valor in jogador.items():
    print(f"O campo {chave} tem o valor {valor}.")
print("-=" * 30)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")
for i, g in enumerate(gols):
    print(f"    => Na partida {i + 1}, fez {g} gols.")
print(f"Foi um total de {jogador['total']} gols.")