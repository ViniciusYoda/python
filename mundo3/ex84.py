pessoas = []
dados = []

while True:
    nome = input("Nome: ")
    peso = float(input("Peso: "))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])  
    dados.clear()  

    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

maior_peso = max(p[1] for p in pessoas)
menor_peso = min(p[1] for p in pessoas)

print(f"\nA) Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"B) As pessoas mais pesadas são: ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"[{p[0]}] ", end="")
print(f"\nC) As pessoas mais leves são: ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"[{p[0]}] ", end="")