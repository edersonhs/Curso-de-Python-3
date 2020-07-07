# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Insira o preço do produto: '))
valorfinal = valor - (5 * valor) / 100

print('{:.2f}R$ com desconto, fica: {:.2f}R$'.format(valor, valorfinal))
