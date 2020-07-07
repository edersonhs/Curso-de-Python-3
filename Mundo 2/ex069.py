MaisDe18 = qtdHomens = qtdMulheresMenos20 = 0
while True:
    print('-' * 35)
    print('{:^35}'.format('CADASTRE UMA PESSOA'))
    print('-' * 35)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
        print('-' * 35)
    if idade >= 18:  # Maiores de 18 anos
        MaisDe18 += 1
    if sexo == 'M':     # Quantidade de Homens
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        qtdMulheresMenos20 += 1     # Quantidade de mulheres com menos de 20 anos
    option = ' '
    while option not in 'SN':
        option = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if option == 'N':
        break
print('Dentre as pessoas cadastradas:')
print(f'{MaisDe18} pessoas tem mais de 18 anos.')
print(f'{qtdHomens} Homens foram cadastrados.')
print(f'{qtdMulheresMenos20} Mulheres tem menos de 20 anos')
