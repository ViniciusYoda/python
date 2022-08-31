x = [39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6]

def media_aritmetica(x):
  N = len(x)
  soma = 0
  for i in range(0, N):
    soma += x[i]
  media = soma / N
  return(media)

def variacao_amostral(x):
  media = media_aritmetica(x)
  N = len(x)
  soma = 0
  for i in range(0, N):
    soma += (x[i] - media)**2 
  varia = soma / (N - 1)
  return(varia)

variacao_amostral([39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6])

def variacao_populacao(x):
  media = media_aritmetica(x)
  N = len(x)
  soma = 0
  for i in range(0, N):
    soma += (x[i] - media)**2 
  varia = soma / N
  return(varia)

variacao_populacao([39, 38, 27, 22, 20, 17, 10, 10, 10, 10, 7, 7, 7, 7, 6])

def desvio_padrao_amostral(x):
  raiz = variacao_amostral(x) ** (1/2)
  return(raiz)

desvio_padrao_amostral(x)

def desvio_padrao_populacao(x):
  raiz = variacao_populacao(x) ** (1/2)
  return(raiz)

desvio_padrao_populacao(x)

def incerteza_media(x):
  N = len(x)
  soma = 0 
  media = media_aritmetica(x)
  for i in range(0, N):
     soma += (x[i] - media)**2 
  varia = soma / (N*(N - 1))
  return(varia)

incerteza_media(x)