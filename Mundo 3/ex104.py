# Crie um programa que tenha a função leiaInt() do python, só que fazendo a validação para aceitar apenas um valor
# númerico.

# ex: n = leiaInt('Digite um n')


def leiaInt(msg):
    """
    -> Um "input" com validação para aceitar apenas números.
    :param msg: mensagem a ser passada ao usúario.
    :return: o número digitado.
    """
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0;0;0m')
    return n


nro = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o múmero {nro}.')
