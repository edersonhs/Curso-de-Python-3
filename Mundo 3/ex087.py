matriz = [[], [], []]
somaPares = somaTerceiraColuna = maiorSegundaLinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somaPares}.')
for l in range(0, 3):
    somaTerceiraColuna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
for c in range(0, 3):
    if c == 0:
        maiorSegundaLinha = matriz[1][c]
    else:
        if matriz[1][c] > maiorSegundaLinha:
            maiorSegundaLinha = matriz[1][c]
print(f'O maior valor da segundo coluna é {maiorSegundaLinha}.')
