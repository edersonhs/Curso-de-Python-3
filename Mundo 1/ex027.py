# Crie um programa que leia o nome completo do usuario e retorne o primeiro e ultimo nome.

nome = str(input('Insira seu nome completo: ')).title().strip()

lista = nome.split()
print('Primeiro nome é: {}'.format(lista[0]))
print('Seu ultimo nome é: {}'.format(lista[nome.count(' ')]))
