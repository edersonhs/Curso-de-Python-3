contador = maior = menor = media = soma = 0
option = 'S'
while option == 'S':
    n = int(input('\033[0;37mDigite um número: '))
    # Verificando o maior número e menor número
    if contador == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    # Coletando dados para calcular média
    soma += n
    contador += 1
    # Verificando se o laço deve continuar
    option = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
# Definindo Média
media = soma / contador
# Apresentando elementos
print('O \033[1;31mMAIOR\033[0;37m elemento lido foi {}'.format(maior))
print('O \033[1;31mMENOR\033[0;37m elemento lido foi {}'.format(menor))
print('Você digitou \033[1;31m{}\033[0;37m números e a média foi \033[1;31m{}\033[0;37m'.format(contador, media))
