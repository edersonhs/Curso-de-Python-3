soma = 0
quantidade = 0
for c in range(3, 501, 6):  # Incrementando o contador de 6 em 6, visto que só aparecem números impares de 6 em 6 posições
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
            quantidade += 1
print('A soma dos {} números impares é {}.'.format(quantidade, soma))
