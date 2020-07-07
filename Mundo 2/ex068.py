from random import randint
qtdVitorias = 0
print('=-'*35)
print('{:^68}'.format('VAMOS JOGAR PAR OU ÍMPAR'))
while True:
    print('=-' * 35)
    PlayerNum = int(input('Diga um número: '))
    IAnum = randint(1, 10)  # Sorteando a jogada da IA
    Total = PlayerNum + IAnum
    Tipo = ' '
    while Tipo not in 'PI':
        Tipo = str(input('Par ou Impar[P/I]?')).strip().upper()[0]
    print('-'*70)
    print(f'Você jogou {PlayerNum} e o compudador jogou {IAnum}. Total de {Total} deu ', end='')
    print('PAR' if Total % 2 == 0 else 'IMPAR')
    print('-'*70)
    if Tipo == 'P':     # PAR
        if Total % 2 == 0:
            print('VOCÊ VENCEU!')
            qtdVitorias += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif Tipo == 'I':   # IMPAR
        if Total % 2 != 0:
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print('=-'*35)
print(f'GAME OVER! Você venceu {qtdVitorias} vezes.')
