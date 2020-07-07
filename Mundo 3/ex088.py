from random import randint
from time import sleep
Jogos = list()
Palpites = list()
qtdJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 10, f'Sorteando {qtdJogos} JOGOS', '-=' * 10)
for Jogo in range(qtdJogos):
    for nroInPalpite in range(6):
        while True:
            nroSorteado = randint(1, 60)
            if nroSorteado not in Palpites:
                Palpites.append(nroSorteado)
                break
    Palpites.sort()
    Jogos.append(Palpites[:])
    Palpites.clear()
for i, l in enumerate(Jogos):
    print(f'Jogo {i+1}: {l} ')
    sleep(1)
print('-=' * 10, ' < BOA SORTE! > ', '-=' * 11)
