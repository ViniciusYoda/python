from datetime import date

def voto(ano_nascimento):
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO."
    elif 16 <= idade < 18 or idade > 70:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

ano = int(input("Em que ano você nasceu? "))
print(voto(ano))