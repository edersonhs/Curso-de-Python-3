# Crie um programa que leia o nome de uma cidade e diga se ela comça ou não com 'Santo'

nome = str(input('Insira o nome da cidade que você nasceu: ')).strip()

lista = nome.split()    # Tranforma cada palavra em uma lista para que possamos verificar se existe 'Santo' na primeira palavra

print('This is {}.'.format('Santo' in lista[0].title()))
