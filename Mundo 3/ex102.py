# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
# a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na
# tela o processo de cálculo do fatorial.


def fatorial(nro, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param nro: o número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um número.
    """
    fat = 1
    for c in range(nro, 0, -1):
        fat *= c
        if show:
            if c != 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    if not show:
        return fat
    else:
        print(fat)


print(fatorial(7, False))
