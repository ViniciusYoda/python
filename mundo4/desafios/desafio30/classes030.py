from hashlib import sha256

class Credencial:
    
    def __init__(self):
        self.__hash = None
        
    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError("A senha não pode ser vazia")
        
    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print("Acesso permitido")
            return True
        else:
            print("Acesso negado")
            return False