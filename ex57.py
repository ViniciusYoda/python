sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f'Sexo registrado com sucesso {sexo}')
