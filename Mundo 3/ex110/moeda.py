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


def resumo(valor=0, aumenta=10, diminui=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(valor):>13}')
    print(f'Dobro do preço: {dobro(valor):>15}')
    print(f'Metade do preço: {metade(valor):>13}')
    print(f'{aumenta}% de aumento: {aumentar(valor, aumenta):>14}')
    print(f'{diminui}% de redução: {diminuir(valor, diminui):>14}')
