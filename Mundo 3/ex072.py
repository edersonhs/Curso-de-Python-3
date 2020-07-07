NumerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro',  'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                     'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('\033[0;30mDigite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente Novamente. ', end='')
    print(f'\033[1;33mVocê digitou o número \033[1;31m{NumerosPorExtenso[n]}.\033[0;30m')
    escolha = str(input('Você quer contiuar[S/N]? ')).strip().upper()[0]
    if escolha == 'N':
        break
