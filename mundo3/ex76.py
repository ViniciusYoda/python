produtos = (
    'Lápis', 1.75,
    'Borracha', 2,
    'Cardeno', 15.90,
    'Estojo', 25,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90,
)

# Cabeçalho
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i + 1]
    print(f'{nome:.<30} R$ {preco:>7.2f}')
print('-' * 40)