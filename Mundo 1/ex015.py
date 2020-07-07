km = float(input('Informe o Km do veículo: '))
dias = int(input('Informe a quantidade de dias que o carro foi alugado: '))

aluguel = dias * 60 + km * 0.15

print('{}'.format('-' *50))
print('Visto que o carro foi alugado por {} dias, e que foram percorridos {:.3f}Km'.format(dias, km))
print('O valor do aluguel será: {:.2f}'.format(aluguel))

