import random

print("=== Gerador de Palpites da Mega Sena ===")
qtd_jogos = int(input("Quantos jogos você quer gerar? "))

if qtd_jogos <= 0:
    print("Por favor, insira um número maior que zero.")
else:
    palpites = []
    for _ in range(qtd_jogos):
        jogo = sorted(random.sample(range(1, 61), 6))
        palpites.append(jogo)

    print("\nSeus palpites:")
    for i, jogo in enumerate(palpites, 1):
        print(f"Jogo {i}: {jogo}")
