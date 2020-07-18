# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

# ex: escreva('Ola, mundo!')

# Saída:
# -----------
# Ola, mundo!
# -----------


def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))


escreva(str(input('Escreva uma mensagem: ')).strip())
