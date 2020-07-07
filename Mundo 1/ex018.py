from math import sin, cos, tan, radians
angulo = float(input('Informe o angulo que você deseja: '))
seno = sin(radians(angulo))   # Foi necessario converter o valor para radianos utilizando a biblioteca radians()
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O angulo de {} tem o Seno de: {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o Cosseno de: {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a Tangente de: {:.2f}'.format(angulo, tangente))
