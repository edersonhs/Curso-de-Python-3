sexo = 'A'

while (sexo != 'F') and (sexo != 'M'):
    sexo = str(input('Insira seu sexo: ')).strip().upper()[0]   # Fatiando a string e pegando apenas o primeiro caractere
    if sexo != 'F' and sexo != 'M':
        print('Sexo invalido. Tente novamente. [M/F]')
print('Sexo {} registrado com sucesso.'.format(sexo))
