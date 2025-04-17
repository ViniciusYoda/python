def notas(*notas, situacao=False):
    """
    Função para analisar notas e situações de vários alunos.

    Parâmetros:
    notas (float): Uma ou mais notas dos alunos (aceita várias).
    situacao (bool): Valor opcional, indicando se deve ou não adicionar a situação.

    Retorno:
    dict: Dicionário com as seguintes informações:
        - quantidade: Quantidade de notas fornecidas.
        - maior: A maior nota.
        - menor: A menor nota.
        - media: A média das notas.
        - situacao (opcional): A situação da turma (Boa, Razoável ou Ruim).
    """
    resultado = {
        'quantidade': len(notas),
        'maior': max(notas) if notas else None,
        'menor': min(notas) if notas else None,
        'media': sum(notas) / len(notas) if notas else 0
    }

    if situacao:
        if resultado['media'] >= 7:
            resultado['situacao'] = 'Boa'
        elif resultado['media'] >= 5:
            resultado['situacao'] = 'Razoável'
        else:
            resultado['situacao'] = 'Ruim'

    return resultado

resp = notas(5.5, 7.0, 8.5, situacao=True)
print(resp)
resp2 = notas(5.5, 7.0, 8.5, 10, situacao=True)
print(resp2)
resp3 = notas(5.5, 7.0, 8.5, 10, 4.5, situacao=True)
print(resp3)