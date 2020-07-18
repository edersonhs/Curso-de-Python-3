# Aprimore o desafio 093 para que ele funcione com vários jogadores. incluindo um sistema de vizualização de detalhes
# do aproveitamento de cada jogador.

jogadores = list()
jogador = dict()
listaGols = list()

while True:
    print('=-' * 32, end='' '=\n')
    jogador['nome'] = str(input('Nome do Jogador: ')).title().strip()
    while True:
        jogador['total'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
        if jogador['total'] <= 8:
            break
        else:
            print('\033[0;31mERRO! Limite de partidas excedido, o limite maximo é 8.\033[0;0;0m')
    for c in range(0, jogador['total']):
        listaGols.append(int(input(f'    > Quantos gols na {c + 1}ª partida? ')))

    temp = gols = ''
    total = 0

    # Transformando a lista de gols em uma string formatada
    for c in listaGols:
        temp += f'{c}' + ', '
        # Calculando total de gols
        total += c
    gols = temp[0:len(gols)-2]
    jogador['gols'] = gols
    jogador['total'] = total

    listaGols.clear()
    jogadores.append(jogador.copy())

    print('-' * 65)
    while True:
        resp = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
        if resp in 'NS':
            break
        print('\033[0;31mERRO! Responda com S ou N.\033[0;0;0m')
    if resp in 'N':
        break

# Sistema de vizualização de detalhes
print('_' * 65)
print(f'|{"Cod":^5}|{"Nome":<25}|{"Gols":<25}|{"Total":^5}|')
print('-' * 65)
for c, v in enumerate(jogadores):
    print(f'|{c:^5}|{jogadores[c]["nome"]:<25}|{jogadores[c]["gols"]:<25}|{jogadores[c]["total"]:^5}|')
print('-' * 65)

while True:
    print('=-' * 32)
    while True:
        cod = int(input('Mostrar dados de qual jogador? '))
        if cod <= len(jogadores) - 1:
            break
        print('\033[0;31mERRO! Jogador não encontrado! Por favor insira um código valido.\033[0;0;0m')
    print(f'    >> Estatísticas do jogador {jogadores[cod]["nome"]}:')

    temp = jogadores[cod]['gols'].replace(' ', '')  # Removendo os espaços
    gols = temp.split(',')  # Transformando em lista

    for c, v in enumerate(gols):
        print(f'        > Na {c + 1}ª partida, {jogadores[cod]["nome"]} fez {v} gols.')
