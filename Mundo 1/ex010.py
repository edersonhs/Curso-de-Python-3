# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela podera comprar.
# Considere: US$1.00 = R$3.27

real = float(input('Insira a quantidade de dinheiro R$ que você possui: R$'))
dolar = real / 3.27
euro = real / 4.63
iene = real / 0.03866
print('Com {:.2f}R$ você pode comprar {:.2f}US$'.format(real, dolar))
print('Com {:.2f}R$ você também pode, comprar {:.2f}€ -> Euros'.format(real, euro))
print('Com {:.2f}R$ você pode comprar também {:.2f}¥ -> Iene '.format(real, iene))


