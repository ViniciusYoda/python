import json
from abc import ABC, abstractmethod
from pathlib import Path
from xml.etree import ElementTree


class Exportavel(ABC):
    @abstractmethod
    def para_dicionario(self):
        pass


class Aluno(Exportavel):
    def __init__(self, nome: str, curso: str, serie: str):
        self.nome = self._validar_texto(nome, "nome")
        self.curso = self._validar_texto(curso, "curso")
        if serie is None:
            raise ValueError("O campo serie deve ser preenchido")
        self.serie = self._validar_texto(str(serie), "serie")

    @staticmethod
    def _validar_texto(valor: str, campo: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"O campo {campo} deve ser preenchido")
        return valor.strip()

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "curso": self.curso,
            "serie": self.serie,
        }


class Usuario(Exportavel):
    def __init__(self, nome: str, email: str):
        self.nome = self._validar_texto(nome, "nome")
        self.email = self._validar_texto(email, "email")

    @staticmethod
    def _validar_texto(valor: str, campo: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(f"O campo {campo} deve ser preenchido")
        return valor.strip()

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "email": self.email,
        }


class Exportador(ABC):
    @abstractmethod
    def exportar(self, objeto: Exportavel, caminho=None):
        pass

    @staticmethod
    def _obter_dados(objeto: Exportavel):
        if not isinstance(objeto, Exportavel):
            raise TypeError("O objeto deve ser Aluno ou Usuario")
        return objeto.para_dicionario()

    @staticmethod
    def _salvar(conteudo: str, caminho):
        if caminho is None:
            return

        arquivo = Path(caminho)
        arquivo.parent.mkdir(parents=True, exist_ok=True)
        arquivo.write_text(conteudo, encoding="utf-8")


class Json(Exportador):
    def exportar(self, objeto: Exportavel, caminho=None):
        dados = self._obter_dados(objeto)
        conteudo = json.dumps(dados, ensure_ascii=False, indent=4)
        self._salvar(conteudo, caminho)
        return conteudo


class Xml(Exportador):
    def exportar(self, objeto: Exportavel, caminho=None):
        dados = self._obter_dados(objeto)
        raiz = ElementTree.Element(objeto.__class__.__name__.lower())

        for campo, valor in dados.items():
            elemento = ElementTree.SubElement(raiz, campo)
            elemento.text = str(valor)

        ElementTree.indent(raiz, space="    ")
        conteudo = ElementTree.tostring(
            raiz,
            encoding="unicode",
            xml_declaration=True,
        )
        self._salvar(conteudo, caminho)
        return conteudo
