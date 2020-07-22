def aumentar(valor=0, porcentagem=0):
    return ((100 + porcentagem) / 100) * valor


def diminuir(valor=0, porcentagem=0):
    return ((100 - porcentagem) / 100) * valor


def dobro(valor=0):
    return valor * 2


def metade(valor=0):
    return valor / 2


def formato(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
