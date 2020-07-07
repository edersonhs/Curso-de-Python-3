numeros = [[], []]
for c in range(0, 7):
    nro = int(input(f'Digite o {c + 1}º número: '))
    if nro % 2 == 0:
        numeros[0].append(nro)  # Par
    else:
        numeros[1].append(nro)  # Impar
print('-=' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
