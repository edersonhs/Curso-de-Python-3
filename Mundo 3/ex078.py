numeros = list()
maior = 0
maiorposi = list()
menor = 0
menorposi = list()

for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}:')))

for pos, num in enumerate(numeros):
    # Verificando Maior
    if numeros[pos] == max(numeros):
        maior = numeros[pos]
    if numeros[pos] == max(numeros):
        maiorposi.append(pos)
    # Verificando Menor
    if numeros[pos] == min(numeros):
        menor = numeros[pos]
    if numeros[pos] == min(numeros):
        menorposi.append(pos)

print(f'Os números digitados foram {numeros}')

print(f'O maior valor digitador foi {maior} nas posições ', end='')
for c in maiorposi:
    print(f'{c}...', end='')

print(f'\nO menor valor digitador foi {menor} nas posições ', end='')
for c in menorposi:
    print(f'{c}...', end='')
