import random
from operator import itemgetter

resultados = {
    f"Jogador {i+1}": random.randint(1, 6)
    for i in range(4)
}

print("Resultados:")
for jogador, resultado in resultados.items():
    print(f"{jogador} tirou {resultado}")

ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

print("\nRanking:")
for posicao, (jogador, resultado) in enumerate(ranking, start=1):
    print(f"{posicao}º lugar: {jogador} com {resultado}")