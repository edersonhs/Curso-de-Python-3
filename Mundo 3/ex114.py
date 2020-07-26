# Crie um código em python que teste se o site Pudim está acessível pelo computador usado.

import requests

try:
    resposta = requests.get('http://www.pudim.com.br/')
except:
    print('\033[31mO site Pudim não esta acessivel no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
