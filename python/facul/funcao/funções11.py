def obter_idade():
    idade = int(input('Digite a sua idade: '))
    return idade

def categoria(idade):
    if idade > 4 and idade < 8:
        msg = 'Infatil A'
    elif idade > 7 and idade < 11:
        msg = 'Infatil B'
    elif idade > 10 and idade < 14:
        msg = 'Juvenil A'
    elif idade > 14 and idade < 18:
        msg = 'Juvenil B'
    else:
        msg = 'Adulto'
    return msg

def principal():
    idade = obter_idade()
    print(categoria(idade)) 

principal()