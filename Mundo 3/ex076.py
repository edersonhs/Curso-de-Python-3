produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*46)
print(f'{"LISTAGEM DE PREÇOS":^46}')
print('-'*46)
for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:.<35} R${produtos[p + 1]:>7.2f}')
print('-'*46)
