n = int(input('Insira um número: '))

'''# METODO USANDO MÓDULOS
from math import factorial
print('O fatorial de {} é {}.'.format(n, factorial(n)))
'''

# MÉTODO USANDO WHILE
f = 1
c = n
print('Calculando o {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c   # Calculando o fatorial
    c -= 1  # Decrementando a variavel de controle
print(f)

'''
# MÉTODO USANDO FOR
f = 1
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c  # Calculando O Fatorial
print(f)
'''