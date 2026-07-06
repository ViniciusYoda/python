import hashlib

texto = "Coração de Leão"
cod = texto.encode('utf-8')
hash = hashlib.sha256(cod).hexdigest()

print(hash)

