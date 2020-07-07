from math import hypot
CatetoOposto = float(input('Insira o comprimento do cateto oposto do triangulo retangulo: '))
CatetoAdjacente = float(input('Insira o comprimento do cateto adjacente do triangulo retangulo: '))

ComprimentoDaHipotenusa = hypot(CatetoOposto, CatetoAdjacente)

print('-' * 70)
print('Sendo o comprimento do cateto oposto dotriangulo retangulo: {}'.format(CatetoOposto))
print('E o compriimento do cateto adjacente do triangulo retangulo: {}'.format(CatetoAdjacente))
print('O comprimento da hipotenusa é: {:.2f}'.format(ComprimentoDaHipotenusa))
