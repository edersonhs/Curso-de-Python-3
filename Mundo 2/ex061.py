print('-=' * 30)
print('{:^60}'.format(' 10 Termos de uma Pregressão Aritimética (Com While)'))
print('-=' * 30)
inicio = int(input('Insira o primeiro termo: '))
intervalo = int(input('Razão: '))
print('-='*30)
c = 1
while c <= 10:
    print('{} -> '.format(inicio) if c < 10 else ' {} '.format(inicio), end='')
    inicio += intervalo
    c += 1
