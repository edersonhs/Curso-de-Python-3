n = soma = qtd = 0
while n != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n < 999:
        soma += n
        qtd += 1
    else:
        print('Você digitou {} numeros e a soma entre eles é {}.'.format(qtd, soma))
