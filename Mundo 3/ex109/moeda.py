def aumentar(valor=0, porcentagem=0, toggleMoeda=True):
    valorAumentado = ((100 + porcentagem) / 100) * valor
    return moeda(valor=valorAumentado, toogle=toggleMoeda)


def diminuir(valor=0, porcentagem=0, toggleMoeda=True):
    valorDiminuido = ((100 - porcentagem) / 100) * valor
    return moeda(valor=valorDiminuido, toogle=toggleMoeda)


def dobro(valor=0, toggleMoeda=True):
    return moeda(valor=valor*2, toogle=toggleMoeda)


def metade(valor=0, toggleMoeda=True):
    return moeda(valor=valor/2, toogle=toggleMoeda)


def moeda(valor=0, moeda='R$', toogle=True):
    if toogle:
        return f'{moeda}{valor:.2f}'.replace('.', ',')
    else:
        return valor
