import re
from abc import ABC, abstractmethod


class ValidadorRegex(ABC):
    @classmethod
    @abstractmethod
    def erros(cls, dado: str):
        pass

    @classmethod
    def validar(cls, dado: str):
        return len(cls.erros(dado)) == 0

    @classmethod
    def validar_ou_erro(cls, dado: str):
        erros = cls.erros(dado)

        if erros:
            raise ValueError("; ".join(erros))

        return True


class ValidadorUsuario(ValidadorRegex):
    PADRAO = re.compile(r"^[a-z0-9_]{5,20}$")

    @classmethod
    def erros(cls, usuario: str):
        if not isinstance(usuario, str):
            return ["O usuario deve ser um texto"]

        erros = []

        if re.fullmatch(r".{5,20}", usuario) is None:
            erros.append("O usuario deve ter entre 5 e 20 caracteres")

        if re.fullmatch(r"[a-z0-9_]+", usuario) is None:
            erros.append(
                "O usuario aceita apenas letras minusculas, numeros e sublinhado"
            )

        return erros


class ValidadorSenha(ValidadorRegex):
    PADRAO = re.compile(r"^(?=\S{8,}$)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]).*$")

    @classmethod
    def erros(cls, senha: str):
        if not isinstance(senha, str):
            return ["A senha deve ser um texto"]

        erros = []

        if re.fullmatch(r".{8,}", senha) is None:
            erros.append("A senha deve ter pelo menos 8 caracteres")

        if re.search(r"[A-Z]", senha) is None:
            erros.append("A senha deve conter pelo menos uma letra maiuscula")

        if re.search(r"[^A-Za-z0-9\s]", senha) is None:
            erros.append("A senha deve conter pelo menos um simbolo")

        if re.search(r"\s", senha) is not None:
            erros.append("A senha nao pode conter espacos")

        return erros


class ValidadorEmail(ValidadorRegex):
    USUARIO_EMAIL = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
    ROTULO_DOMINIO = r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    PADRAO = re.compile(
        rf"^(?:{USUARIO_EMAIL})(?:\.{USUARIO_EMAIL})*"
        rf"@(?:{ROTULO_DOMINIO}\.)+[A-Za-z]{{2,}}$"
    )

    @classmethod
    def erros(cls, email: str):
        if not isinstance(email, str):
            return ["O email deve ser um texto"]

        if email.count("@") != 1:
            return ["O email deve conter uma unica arroba (@)"]

        usuario, dominio = email.split("@")
        erros = []
        padrao_usuario = re.compile(
            rf"^(?:{cls.USUARIO_EMAIL})(?:\.{cls.USUARIO_EMAIL})*$"
        )
        padrao_dominio = re.compile(
            rf"^(?:{cls.ROTULO_DOMINIO}\.)+[A-Za-z]{{2,}}$"
        )

        if padrao_usuario.fullmatch(usuario) is None:
            erros.append("O usuario do email possui caracteres ou pontos invalidos")

        if padrao_dominio.fullmatch(dominio) is None:
            erros.append(
                "O dominio deve conter ponto e terminar com pelo menos duas letras"
            )

        return erros
