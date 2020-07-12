# Crie um programa onde 4 jogadores joguem um dado e tenham um resultado aleatório (de 1 a 6).
# Guarde esses resultados em um dicionário e no final, coloque esse dicionário em ordem.
# Sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter     # Serve para retirar o item de uma posição do index

jogo = dict()
ranking = list()

for c in range(1, 5):
    jogadores = str('jogador') + str(c)
    jogo[jogadores] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogo.items():
    sleep(1)
    print(f'    O {k} tirou {v}')

# ordenando o dicionario "jogo" no dicionario "ranking"  pelo  item UM, que nesse caso, refere-se aos valores do dado.
# (o item ZERO seriam os nomes dos jogadores)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('=-' * 30, f'\n{" RANKING ":%^35}')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
