soma = 0
for c in range(0, 6):
    numero = int(input('Insira o {}º número inteiro: '.format(c + 1)))
    if numero % 2 == 0:
        soma += numero
print('A soma de todos os números pares inseridos é {}'.format(soma))
