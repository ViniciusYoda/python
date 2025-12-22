try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError) as e:
    print(f'Tivemos um problema com o tipo de dado que você digitou. Erro: {e}')
except ZeroDivisionError as e:
    print(f'Não é possível dividir um número por zero. Erro: {e}')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as e:
    print(f'Erro desconhecido. Erro: {e}')
else:
    print('Tudo certo, conseguimos fazer a divisão!')
finally:
    print('Volte sempre! Muito obrigado!')


print(f'O resultado é {r}')