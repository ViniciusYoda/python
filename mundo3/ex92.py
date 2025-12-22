from datetime import datetime

dados = {}

dados['nome'] = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - ano_nascimento
dados['ctps'] = int(input("Carteira de Trabalho (0 se não tem): "))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$ "))
    dados['aposentadoria'] = dados['idade'] + (35 - (datetime.now().year - dados['ano_contratacao']))

print("-=" * 30)
for chave, valor in dados.items():
    print(f"{chave}: {valor}")