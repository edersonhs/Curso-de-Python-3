# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    areaTerreno = largura * comprimento
    print(f'A área de um terrono {largura}x{comprimento} é de {areaTerreno:.1f}m².')


area(float(input('Largura (m): ')), float(input('Comprimento(m): ')))
