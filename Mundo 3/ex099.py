# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def maior(* valores):
    print('=-' * 30)
    print('Analisando os valores informados...')
    for c in valores:
        sleep(0.5)
        print(f'{c} ', end='')
    sleep(0.5)
    print(f'|| Foram informados {len(valores)} valores ao todo.')
    print(f'      > O maior valor informado foi {max(valores)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)