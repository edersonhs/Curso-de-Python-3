matriz = [[], [], []]

for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))
print('-=' * 30)
print('Matriz:')
for lista in range(0, 3):
    for nro in range(0, 3):
        print(f'[{matriz[lista][nro]:^5}]', end='')
    print()
