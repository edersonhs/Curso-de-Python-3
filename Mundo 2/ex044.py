print('\033[1;33m-\033[1;35m=\033[1;33m' * 40)
print('{:=^80}'.format(' A K I O\'S M A R K E T P L A C E '))
print('\033[1;33m-\033[1;35m=' * 40)
ValorCompra = float(input('\033[1;30mPreço das compras: R$'))
print('Como pretende pagar?')
print('[ 1 ] A Vista. [Dinheiro / Cheque]')
print('[ 2 ] A Vista no Cartão.')
print('[ 3 ] 2x no Cartão.')
print('[ 4 ] 3x ou Mais no Cartão.')
escolha = int((input('Sua escolha: ')))

if escolha == 1:
    ValorCompraDesc = ValorCompra - (ValorCompra * 10 / 100)
    print('A compra de {} vai custar {}. (10% de desconto)'.format(ValorCompra, ValorCompraDesc))
elif escolha == 2:
    ValorCompraDesc = ValorCompra - (ValorCompra * 5 / 100)
    print('A compra de {} vai custar {}. (5% de desconto)'.format(ValorCompra, ValorCompraDesc))
elif escolha == 3:
    print('A compra de {} vai ficar {}. (Sem desconto)'.format(ValorCompra, ValorCompra))
elif escolha == 4:
    juro = ValorCompra + (ValorCompra * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(parcelas, juro / parcelas))
    print('A compra de {} vai ficar {}. (20% de juros)'.format(ValorCompra, juro))
else:
    print('Opção invalida. Tente novamente.')
