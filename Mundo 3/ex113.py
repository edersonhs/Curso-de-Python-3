# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
# tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    """
    -> Um "input" com validação para aceitar apenas números inteiros.
    :param msg: mensagem a ser passada ao usúario.
    :return: o número digitado.
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[0;0;0m')
            continue    # volta pro while
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    """
    -> Um "input" com validação para aceitar apenas números reais.
    :param msg: mensagem a ser passada ao usúario.
    :return: o número digitado.
    """
    while True:
        try:
            n = float(str(input(msg)).strip().replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[0;0;0m')
            continue  # volta pro while
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


numeroInteiro = leiaInt('Digite um número inteiro: ')
numeroReal = leiaFloat('Digite m número Real: ')

print(f'O valor inteiro digitado foi {numeroInteiro} e o real foi {numeroReal}.')
