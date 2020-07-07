print('-='*20)
print('\033[1;35mAnalisador de Triângulos 2.0\033[m')
print('-='*20)
lado1 = float(input('Insira o tamanho do 1º lado: '))
lado2 = float(input('Insira o tamanho do 2º lado: '))
lado3 = float(input('Insira o tamanho do 3º lado: '))

if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado3 + lado2) > lado1):
    print('Os segmentos acima podem formar um triângulo.')
    if lado1 == lado2 and lado1 == lado3:
        print('E o tipo do triângulo é: \033[1;33mEQUILÁTERO\033[m')
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado3 == lado2 and lado3 != lado1):
        print('E o tipo do triângulo é: \033[1;33mISÓSCELES\033[m')
    else:
        print('E o tipo do triângulo é: \033[1;33mESCALENO\033[m')
else:
    print('\033[1;31mOs segmentos acima não podem formar um triângulo.')
