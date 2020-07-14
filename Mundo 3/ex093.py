# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do
# jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = list()
total = 0

jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, partidas):
    gols.append(int(input(f"    Quantos gols na {c+1}ª partida? ")))
jogador['gols'] = gols[:]

for qtdGols in jogador['gols']:
    total += qtdGols    # Poderia substituir por: jogador['total'] = sum(gols)
jogador['total'] = total

print('=-' * 30)
print(jogador)

print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-=' * 30)
print(f"O jogador {jogador['nome']} jogou {partidas} partidas.")  # Poderia substituir {partidas} por {len(jogador['gols']}
for c, v in enumerate(jogador['gols']):
    print(f'    => Na {c+1}ª partida, fez {v} gols.')
print(f"Foi um total de {jogador['total']} gols.")
