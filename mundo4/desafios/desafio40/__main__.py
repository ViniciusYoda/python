from pathlib import Path

from classes040 import Aluno, Json, Usuario, Xml


def main():
    aluno = Aluno("Ana Souza", "Desenvolvimento de Sistemas", "3A")
    usuario = Usuario("Carlos Lima", "carlos@example.com")

    exportadores = {
        "json": Json(),
        "xml": Xml(),
    }
    objetos = {
        "aluno": aluno,
        "usuario": usuario,
    }
    pasta = Path(__file__).parent / "exportacoes"

    for nome_objeto, objeto in objetos.items():
        for extensao, exportador in exportadores.items():
            arquivo = pasta / f"{nome_objeto}.{extensao}"
            conteudo = exportador.exportar(objeto, arquivo)
            print(f"\n{arquivo.name}")
            print(conteudo)

    print(f"\nArquivos salvos em: {pasta}")


if __name__ == "__main__":
    main()
