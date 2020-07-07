from random import shuffle

nome1 = input('Insira o primeiro nome: ')
nome2 = input('Insira o segundo nome: ')
nome3 = input('Insira o terceiro nome:')
nome4 = input('Insira o quarto nome: ')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem sorteada foi {}'.format(lista))
