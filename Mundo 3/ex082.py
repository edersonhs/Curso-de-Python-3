listNumeros = list()
listPares = list()
listImpares = list()

while True:
    listNumeros.append(int(input('Digite um número: ')))
    opt = input('Quer continuar? [S/N] ')
    if opt in 'nN':
        break
for c in range(0, len(listNumeros)):
    if listNumeros[c] % 2 == 0:
        listPares.append(listNumeros[c])
    else:
        listImpares.append(listNumeros[c])
print('=-' * 30)
print(f'A lista completa é: {listNumeros}')
print(f'A lista de pares é: {listPares}')
print(f'A lista de impares é: {listImpares}')
