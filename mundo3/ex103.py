def ficha(nome='<desconhecido>', gols=0):
    """
    Exibe a ficha de um jogador com seu nome e número de gols.
    
    :param nome: Nome do jogador (opcional, padrão é '<desconhecido>').
    :param gols: Número de gols marcados (opcional, padrão é 0).
    """
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = input('Nome do jogador: ').strip()
gols_jogador = input('Número de gols: ').strip()

if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)