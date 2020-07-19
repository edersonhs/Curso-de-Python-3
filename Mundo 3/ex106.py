# Faça um mini-sistema que utilize o intreractive Help do Python. O usuário vai digitar  o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerra.    obs: Use cores


def letreiro(msg, tipoFonte='', corFonte='', corFundo=''):
    """
    -> Função que moonta um letreiro.
    :param msg: Mensagem a ser apresentada no letreiro.
    :param tipoFonte: Tipo da fonte (0 = none, 1 = bold, 4 = underline, 7 = negative)
    :param corFonte: Cor da fonte (30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = roxo, 36 = azul ciano, 37 = cinza)
    :param corFundo: Cor do fundo (40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = roxo, 46 = azul ciano, 47 = cinza)
    :return: Não retorna nada.
    """
    print(f'\033[{tipoFonte};{corFonte};{corFundo}m', end='')
    print('~' * 140)
    print(f'{msg:^140}')
    print('~' * 140)
    print('\033[m')


def dicionarioPython(pesquisa):
    from time import sleep
    if pesquisa.upper() == 'FIM':
        letreiro('ATÉ LOGO!', '1', '30', '45')
        sleep(3)
        for c in range(0, 50):
            print('\n')
            sleep(0.010)
        exit()
    letreiro(f'Acessando o manual do comando {pesquisa.title()}', '1', '30', '44')
    sleep(0.5)
    help(pesquisa)


while True:
    letreiro('SISTEMA DE AJUDA PyHelp', '1', '30', '47')
    dicionarioPython(str(input('Função ou Biblioteca: ')))  # Fim para sair
