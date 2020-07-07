import random
nome1 = input('Insira o primeiro nome: ')
nome2 = input('Insira o segundo nome: ')
nome3 = input('Insira o terceiro nome: ')
nome4 = input('Insira o quarto nome:  ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

# Pode ser escrito assim:
# print('O aluno sorteado foi: {}'.format(escolhido))
# Ou...........
print('O aluno sorteado foi: {}'.format(random.choice([nome1, nome2, nome3, nome4])))
