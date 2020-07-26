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


def linha(tam=45):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(45))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} \033[m- \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua opção: \033[m')
    return opc