# Sequência de Fibonacci

print('-='*30)
print('{:^60}'.format('Sequência de Fibonacci'))
print('-='*30)
termos = int(input('Quantos termos você quer mostrar? '))
count = 3
termo1 = 0
termo2 = 1
print('{} -> {} -> '.format(termo1, termo2),end='')
while count <= termos:
    termo3 = termo1 + termo2
    if count < termos:
        print('{} -> '.format(termo3), end='')
    else:
        print('{}'.format(termo3))
    termo1 = termo2
    termo2 = termo3
    count += 1
print('\nend')
