nome = str(input('Qual seu nome completo: ')).strip()

print('Seu nome é: {}.'.format(nome.title()))
print('Seu nome com todas as letras maiusculas é: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minusculas é: {}.'.format(nome.lower()))

tamanho = nome.split()
print('O seu nome possui {} caracteres.'.format(len(''.join(tamanho))))
#   print('O seu nome possui {} caracteres.'.format(len(nome) - nome.count(' ')) //// retorna o número de caracteres do nome - a quantidade de espaços
print('Seu primeiro nome é: {} e ele tem {} letras.'.format(tamanho[0], len(tamanho[0])))
