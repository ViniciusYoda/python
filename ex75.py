values = (
    int(input("Digite o primeiro valor: ")),
    int(input("Digite o segundo valor: ")),
    int(input("Digite o terceiro valor: ")),
    int(input("Digite o quarto valor: "))
)
count_nine = values.count(9)
print(f"O valor 9 apareceu {count_nine} vezes.")
if 3 in values:
    first_three_position = values.index(3) + 1
    print(f"O primeiro valor 3 foi digitado na posição {first_three_position}.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
even_numbers = [num for num in values if num % 2 == 0]
print(f"Os números pares digitados foram: {even_numbers}")