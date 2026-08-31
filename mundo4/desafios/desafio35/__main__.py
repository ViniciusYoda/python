from classes035 import DOC, PDF


def main():
    arquivos = [
        PDF("apostila", 2_500),
        DOC("relatorio", 800),
    ]

    for arquivo in arquivos:
        print(arquivo.abrir())


if __name__ == "__main__":
    main()
