print('\033[1;30mCalculadora de IMC')
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura*altura)
print('Seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('E você esta Abaixo do Peso.')
elif imc <= 25:
    print('E você esta no Peso Ideal.')
elif imc < 30:
    print('E você esta com Sobrepeso.')
elif imc < 40:
    print('E você esta com Obesidade.')
else:
    print('E você esta com Obesidade Morbida.')
