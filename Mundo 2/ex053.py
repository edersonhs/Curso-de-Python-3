print('\033[1;33m-\033[1;31m='*20)
print('{:=^40}'.format(' Detector de Palindromo '))
print('\033[1;33m-\033[1;31m='*20)

Frase = str(input('\033[0;30mInsira uma frase: ')).strip().upper().split(' ')   # Transforma a frase em uma lista com cada palavra
FraseJunta = ''.join(Frase)     # Usando Join() Para juntar todas as palavras da lista
FraseInvertida = ''
for c in range(len(FraseJunta) - 1, -1, -1):
    FraseInvertida += FraseJunta[c]
print('O inverso de {} é {}'.format(FraseJunta, FraseInvertida))

if FraseJunta == FraseInvertida:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo.')

