print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
lado1 = float(input('Insira o tamanho do 1º lado: '))
lado2 = float(input('Insira o tamanho do 2º lado: '))
lado3 = float(input('Insira o tamanho do 3º lado: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')
