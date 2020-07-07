print('-=' * 30)
print('{:^60}'.format(' 10 Termos de uma Pregressão Aritimética '))
print('-=' * 30)
inicio = int(input('Primeiro Termo: '))
intervalo = int(input('Razão: '))
for c in range(0, 10):
    if c < 9:
        print('{} ->'.format(inicio), end=' ')
    else:
        print('{}'.format(inicio))
    inicio += intervalo
print('End.')
