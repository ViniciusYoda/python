people = []
while True:
    person = {}
    person['name'] = input("Nome: ").strip()
    person['sex'] = input("Sexo (M/F): ").strip().upper()
    while person['sex'] not in 'MF':
        print("Erro! Por favor, digite apenas M ou F.")
        person['sex'] = input("Sexo (M/F): ").strip().upper()
    person['age'] = int(input("Idade: "))
    people.append(person)
    
    continue_response = input("Quer continuar? (S/N): ").strip().upper()
    while continue_response not in 'SN':
        print("Erro! Responda apenas S ou N.")
        continue_response = input("Quer continuar? (S/N): ").strip().upper()
    if continue_response == 'N':
        break

print(f"A) Total de pessoas cadastradas: {len(people)}")

average_age = sum(person['age'] for person in people) / len(people)
print(f"B) A média de idade é: {average_age:.2f} anos")

women = [person['name'] for person in people if person['sex'] == 'F']
print(f"C) Lista de mulheres: {', '.join(women) if women else 'Nenhuma mulher cadastrada'}")

above_average = [person for person in people if person['age'] > average_age]
print("D) Lista de pessoas com idade acima da média:")
for person in above_average:
    print(f"   Nome: {person['name']}, Sexo: {person['sex']}, Idade: {person['age']}")