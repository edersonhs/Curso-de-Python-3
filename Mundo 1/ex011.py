# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m².

altura = float(input('Insira a altura da parede(m): '))
largura = float(input('Insira a largura da parede(m): '))

m2 = altura * largura
tinta = m2 / 2

print('Levanto em conta que a parede tem {:.2f}m², serão necessarios {:.4f}L de tinta para pintar a parede.'.format(m2, tinta))
