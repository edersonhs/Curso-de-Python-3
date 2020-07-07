# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
dobro = 2*n
triplo = 3*n
raiz = n**(1/2)

print('O dobro de {} é: {}'.format(n, dobro))
print('O triplo de {} é: {}'.format(n, triplo))
print('A raiz de {} é: {:.2f}'.format(n, raiz))
