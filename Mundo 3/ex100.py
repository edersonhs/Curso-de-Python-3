# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai coloca-los dentro da lista e a segunda vai mostrar a soma entre todos os valores PARES
# sorteados pela função anterior.

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0, 5):
        sleep(0.5)
        lista.append(randint(1, 10))
        print(f'{lista[len(lista) - 1]} ', end='')
    sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    Soma = 0
    for n in lista:
        if n % 2 == 0:
            Soma += n
    print(f'Somando os valores pares de {lista}, temos {Soma}.')


numeros = []

sorteia(numeros)
somaPar(numeros)
