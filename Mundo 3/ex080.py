lista = list()

for c in range(0, 5):
    n = int(input('Digite um número:'))
    # verificando se é o primeiro número a ser adicionado na lista.
    # Verificando também se é o ultimo elemento da lista. ([-1] indica a ultima posição da lista.)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao fim da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            # Se numero digitado for menor ou igual ao número sendo verificado no memomento, inserir n na posição atual.
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1
print(f'Lista: {lista}')

######################################################################
# PRIMEIRA TENTATIVA DE CÓDIGO
######################################################################
# lista = list()
#
# for d in range(0, 5):
#     n = int(input('Digite um número: '))
#     if len(lista) < 2:
#         if len(lista) == 0:
#             lista.append(n)
#             print('Adicionado na posição 0...')
#         elif len(lista) == 1:
#             if lista[0] < n:
#                 lista.append(n)
#                 print('Adicionado ao fim da lista...')
#             else:
#                 lista.insert(0, n)
#                 print('Adicionado na posição 0...')
#     if len(lista) >= 2:
#         for c in range(0, len(lista) - 1):
#             if lista[c] < n < lista[c + 1]:
#                 lista.insert(c + 1, n)
#                 print(f'Adicionado na posição {c + 1}...')
#             elif n > max(lista):
#                 lista.append(n)
#                 print('Adicionado ao fim da lista...')
#             elif n < min(lista):
#                 lista.insert(0, n)
#                 print('Adicionado na posição 0...')
# print(f'\nLista = {lista}')
########################################################################
