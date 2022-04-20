    executa = input('Executar o bloco (sim/nao): ')
    contador = 0
    while executa == 'sim':
        contador += 1
        executa = input("Executar o bloco (sim/nao): ")

    print(f'O bloo foi executado {contador} vezes')