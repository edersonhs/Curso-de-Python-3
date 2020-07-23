# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função formato(), desenvolvida no desafio 108.

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, False)}.')
print(f'Aumentando 10% de {moeda.moeda(preco)}, temos {moeda.aumentar(preco, 10, False)}.')
print(f'Diminuindo 13% de {moeda.moeda(preco)}, temos {moeda.diminuir(preco, 13, True)}.')
