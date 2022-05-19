#criando e inicializando listas
lista = []
lista = 10
lista = ['frio', 123, 'fiap', True]
nova_lista = ['frio', 123]
lista.append(nova_lista)
nova_lista.append('calor')
print(lista)
print(nova_lista)
print(lista[4][0])
print(len(lista))
print(len(nova_lista))
soma = lista + nova_lista
print(soma)
multi = lista * 3
print(multi)
teste = 'fiap' in lista
print(teste)
ponto = 'calor' in lista
print(ponto)

numeros = [14, 44, 55, 67, 88, 10, 21, 5]
print(min(numeros))
print(max(numeros))
print(sum(numeros))

livros = ['Java', 'Python', 'SQL Server', 'ios']
livros.append('Android')
print(livros)
livros.insert(0,'Oracle')
print(livros)
livros.pop(1)
print(livros)
livros.extend('von')
print(livros)
livros.remove('ios')
print(livros)
livros.reverse()
print(livros)
livros.sort()
print(livros)
numeros.sort()
print(numeros)
le = ord('$')
print(le)
pe = chr(4)
print(pe)
print('Hoje eu estou ' + chr(4))
numeros = [2, 5, 8, 7, 10, 2, 2, -5, 10]
cont = numeros.count(2)
print(cont)
n = [1,2,3]
m = [4,5,6]
n.extend(m)
print(n)
