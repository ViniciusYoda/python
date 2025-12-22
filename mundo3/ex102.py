def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.

    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O fatorial do número.
    """
    resultado = 1
    for i in range(num, 0, -1):
        resultado *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return resultado

print(fatorial(8))
print(fatorial(5, show=True))