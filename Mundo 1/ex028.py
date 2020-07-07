from random import randint
from time import sleep

resposta = randint(0, 5)
print('''\033[1;33m
       _                         _                  _ _       _       _                             __   ___  
      | |                       | |                | (_)     (_)     | |                           /_ | / _ \ 
      | | ___   __ _  ___     __| | ___    __ _  __| |___   ___ _ __ | |__   __ _  ___ __ _  ___    | || | | |
  _   | |/ _ \ / _` |/ _ \   / _` |/ _ \  / _` |/ _` | \ \ / / | '_ \| '_ \ / _` |/ __/ _` |/ _ \   | || | | |
 | |__| | (_) | (_| | (_) | | (_| |  __/ | (_| | (_| | |\ V /| | | | | | | | (_| | (_| (_| | (_) |  | || |_| |
  \____/ \___/ \__, |\___/   \__,_|\___|  \__,_|\__,_|_| \_/ |_|_| |_|_| |_|\__,_|\___\__,_|\___/   |_(_)___/ 
                __/ |                                                                                         
               |___/                                                                                          
\033[m''')
print('\033[1;33m-\033[1;31m=' * 30)
print('\033[33;1mVou pensar em um número entre 0 e 5, tente adivinhar... ')
print('\033[1;33m-\033[1;31m=' * 30)
n = int(input('Em que número eu pensei? '))
print('Processando\033[1;33m.\033[1;31m.\033[1;33m.')
sleep(3)
if n == resposta:
    print('\033[1;33mPARABÉNS! Você conseguiu me vencer! Eu pensei no número {}.'.format(resposta))
else:
    print('\033[1;33mGANHEI! Eu pensei no número {} e não no {}.'.format(resposta, n))
