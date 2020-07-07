# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = str(input('Insira seu nome: ')).title().strip().split()

print('This is {}'.format('Silva' in nome))
