# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.


def ficha(name, gols=0):
    if len(name) == 0:
        name = '<Desconhecido>'
    if len(gols) == 0:
        gols = '0'
    print(f'O jogador {name} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).title().strip()

qtdGols = str(input('Número de Gols: ')).strip()
if qtdGols.isnumeric():
    qtdGols = int(qtdGols)
else:
    gols = 0

ficha(nome, qtdGols)
