# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize
# a contagem.

# Seu programa tem que realizar três contagens através da função criada:

# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada.

from time import sleep as pausa


def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            pausa(0.5)
            print(f'{c} ', end='')
    else:
        for c in range(inicio, fim - 1, -passo):
            pausa(0.5)
            print(f'{c} ', end='')
    pausa(0.5)
    print('FIM!')


print('=-' * 30)
contador(1, 10, 1)

print('=-' * 30)
contador(10, 0, 2)

print('=-' * 30)
print('Contagem personalizada:')
begin = int(input('Inicio: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
if step < 0:
    step *= -1
elif step == 0:
    step = 1

print('=-' * 30)
contador(begin, end, step)
