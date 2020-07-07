termo1 = termo3 = c = 0
termo2 = 1
termos = int(input('Quantos termos você quer mostrar: '))
print('{} -> {} -> '.format(termo1, termo2), end='')
for c in range(3, termos + 1):
    termo3 = termo1 + termo2
    print('{} -> '.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
print('Fim')
