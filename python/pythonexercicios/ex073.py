times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Refife', 'EC Vitória', 'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')
print('-='*80)
print(f'Lista de times : {times}')
print('-='*80)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*80)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('-='*80)
print(f'Times em ordem alfábetica {sorted(times)}')
print('-='*80)
print(f'Chapecoense está na {times.index("Chapecoense") + 1} posição')
print('-='*80)
