# CAMPEONATO BRASILEIRO DE FUTEBOL - SÉRIE A - 2019
classeA = ('Flamengo - RJ', 'Santos - SP', 'Palmeiras - SP', 'Grêmio - RS', 'Athletico Paranaense - PR',
           'São Paulo - SP', 'Internacional - RS', 'Corinthians - SP', 'Fortaleza - CE', 'Goiás - GO',
           'Bahia - BA', 'Vasco da Gama - RJ', 'Atlético - MG', 'Fluminense - RJ', 'Botafogo - RJ', 'Ceará - CE',
           'Cruzeiro - MG', 'Csa - AL', 'Chapecoense - SC', 'Avaí - SC')
print('=-'*200)
print(f'Lista de times do Brasileirão: {classeA}')
print('=-'*200)
print(f'Os 5 primeiros são {classeA[:5]}')
print('=-'*200)
print(f'Os 4 Ultimos são {classeA[-4:]}')
print('=-'*200)
print(f'Times em ordem alfabética: {sorted(classeA)}')
print('=-'*200)
print('A Chapecoense esta na {}ª posição.'.format(classeA.index('Chapecoense - SC') + 1))
print('=-'*200)
