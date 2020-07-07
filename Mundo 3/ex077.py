palavras = ('aprender', 'progamar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print('-'*45)
print(f'{"ANALISANDO VOGAIS":^45}')
print('-'*45)
for palavra in palavras:    # Navegando por cada palavra
    if palavra == palavras[0]:
        print(f'Na palavra {palavra.upper()} temos ', end='')
    else:
        print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in range(0, len(palavra)):    # Navegando por cada letra da palavra
        if palavra[letra] == 'a':
            print('a ', end='')
        elif palavra[letra] == 'e':
            print('e ', end='')
        elif palavra[letra] == 'i':
            print('i ', end='')
        elif palavra[letra] == 'o':
            print('o ', end='')
        elif palavra[letra] == 'u':
            print('u ', end='')
