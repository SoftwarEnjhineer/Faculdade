times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio',
         'Bahia', 'Sport Recife', 'Chapecoense')


print(times)


print(f'Os classificado para a Copa Libertadores são {times[0:5]}')


print(f'Os quatro times rebaixados foram {times[-4:]}')


print(f'Os times em ordem alfabética são {sorted(times)}')


print(f'A Chapecoense ficou em {times.index("Internacional")+ 1}º lugar')
