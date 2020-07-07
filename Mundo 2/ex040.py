# Calcula média e retorna REPROVADO / RECUPERAÇÃO / APROVADO.
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('\033[30;1mTirando {:.1f} e {:.1f} a média é {:.1f}.'.format(nota1, nota2, media))
if media < 5.0:
    print('\033[1;31mO aluno esta REPROVADO')
elif (media >= 5.0) and (media < 7.0):
    print('\033[1;33mO aluno esta de RECUPERAÇÃO.')
else:
    print('\033[1;32mO aluno esta APROVADO')
