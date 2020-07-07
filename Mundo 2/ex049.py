numero = int(input('Insira um número para o qual deseja calcular a tabuada: '))
for c in range(1, 10 + 1):
    print("{} x {:2} = {}".format(numero, c, numero * c))
