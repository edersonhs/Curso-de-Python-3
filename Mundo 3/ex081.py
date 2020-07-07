listNumeros = list()
nElementos = 0

while True:
    listNumeros.append(int(input('Digite um valor: ')))
    opt = str(input('Quer continuar? [S/N] '))
    nElementos += 1
    if opt in 'nN':
        break
listNumeros.sort(reverse=True)
print(f'Você digitou {nElementos} elementos.')
print(f'Os valores em ordem decrescente são {listNumeros}')
if 5 in listNumeros:
    print('O valor 5 faz parte da lista e esta nas posições ', end='')
    for pos, nro in enumerate(listNumeros):
        if nro == 5:
            print(f'{pos}, ', end='')
else:
    print('O valor 5 não faz parte da lista!')
