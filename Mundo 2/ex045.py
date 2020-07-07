from time import sleep
import random
cores = {'yellow': '\033[1;33m',
         'cyan': '\033[1;36m',
         'white': '\033[1;30m',
         'clear': '\033[m'}
print('''{}
    /$$$$$                 /$$   /$$                           /$$$$$$$          
   |__  $$                | $$  /$$/                          | $$__  $$         
      | $$  /$$$$$$       | $$ /$$/   /$$$$$$  /$$$$$$$       | $$  \ $$ /$$$$$$ 
      | $$ /$$__  $$      | $$$$$/   /$$__  $$| $$__  $$      | $$$$$$$//$$__  $$
 /$$  | $$| $$  \ $$      | $$  $$  | $$$$$$$$| $$  \ $$      | $$____/| $$  \ $$
| $$  | $$| $$  | $$      | $$\  $$ | $$_____/| $$  | $$      | $$     | $$  | $$
|  $$$$$$/|  $$$$$$/      | $$ \  $$|  $$$$$$$| $$  | $$      | $$     |  $$$$$$/
 \______/  \______/       |__/  \__/ \_______/|__/  |__/      |__/      \______/ 
{}'''.format(cores['yellow'], cores['clear']))
choice = int(input('{}[ 1 ]{} Pedra.'
                   '\n{}[ 2 ]{} Papel.'
                   '\n{}[ 3 ]{} Tesoura.'
                   '\nSua escolha: '.format(cores['cyan'], cores['white'], cores['cyan'], cores['white'], cores['cyan'], cores['white'])))
if choice > 3 or choice < 1:
    print('Opção invalida, tente novamente.')
    exit()
else:
    print('\033[1;35m')
    print('''
    /$$$$$          
   |__  $$          
      | $$  /$$$$$$ 
      | $$ /$$__  $$
 /$$  | $$| $$  \ $$
| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/
 \______/  \______/ 
''', end='')  # JO
    sleep(1)
    print('\033[1;32m')
    print('''
 /$$   /$$                    
| $$  /$$/                    
| $$ /$$/   /$$$$$$  /$$$$$$$ 
| $$$$$/   /$$__  $$| $$__  $$
| $$  $$  | $$$$$$$$| $$  \ $$
| $$\  $$ | $$_____/| $$  | $$
| $$ \  $$|  $$$$$$$| $$  | $$
|__/  \__/ \_______/|__/  |__/
''', end='')  # KEN
    sleep(1)
    print('\033[1;31m')
    print('''
 /$$$$$$$          
| $$__  $$         
| $$  \ $$ /$$$$$$ 
| $$$$$$$//$$__  $$
| $$____/| $$  \ $$
| $$     | $$  | $$
| $$     |  $$$$$$/
|__/      \______/ 
''')    # PO
    sleep(1)
    IAChoice = random.choice(['Pedra', 'Papel', 'Tesoura'])  # Sorteando a jogada da máquina
    print('{}-{}='.format(cores['cyan'], cores['white']) * 20, end='')
    print('{}'.format(cores['yellow']))
    if choice == 1 or IAChoice == 1:
        choice = 'Pedra'
    elif choice == 2:
        choice = 'Papel'
    else:
        choice = 'Tesoura'
        # Vitórias do Player
    if IAChoice == choice:
        print('Empate! Eu Joguei {} e você também jogou {}.'.format(IAChoice, choice))
    elif IAChoice == 'Pedra' and choice == 'Papel':
        print('Você Ganhou!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
    elif IAChoice == 'Papel' and choice == 'Tesoura':
        print('Você Ganhou!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
    elif IAChoice == 'Tesoura' and choice == 'Pedra':
        print('Você Ganhou!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
    # Vitorias da máquina
    elif IAChoice == 'Papel' and choice == 'Pedra':
        print('Você Perdeu!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
    elif IAChoice == 'Tesoura' and choice == 'Papel':
        print('Você Ganhou!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
    elif IAChoice == 'Pedra' and choice == 'Tesoura':
        print('Você Ganhou!'
              '\nSua Jogada: {}.'
              '\nMinha jogada: {}.'.format(choice, IAChoice))
exit()
