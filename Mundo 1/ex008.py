# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = int(input('Insira um valor em metros: '))
cm = m/0.01
mm = m/0.001
km = m/1000

print('{:.1f}m em centimetros é: {:.0f}cm'.format(m, cm))
print('{:.1f}m em milimetro è: {:.0f}mm'.format(m, mm))
print('{:.1f}m em quilometros é: {:.3f}km'.format(m, km))


