frase = str(input('Insira uma frase: ')).strip().lower()

print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A primeira letra "A" apareceu na posição {}.'.format(frase.find('a') + 1))
print('A ultima letra "A" aparece na posição {}'.format(frase.rfind('a') + 1))
