MenorPeso = 0
MaiorPeso = 0
for c in range(0, 5):
    Peso = float(input('Insira o {} peso:'.format(c + 1)))
    if c == 0:
        MenorPeso = Peso
    elif Peso < MenorPeso:
        MenorPeso = Peso
    elif Peso > MaiorPeso:
        MaiorPeso = Peso
print('O maior peso foi {}Kg'.format(MaiorPeso))
print('O menor peso foi {}Kg'.format(MenorPeso))
