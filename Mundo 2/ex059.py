from time import sleep
n1 = float(input('\033[30mInsira um número: '))
n2 = float(input('Insira outro número: '))
print('\033[31m-\033[33m='*20)
option = 0
while option != 5:
    print('\033[1;33m[ 1 ] Somar.'
          '\n[ 2 ] Multiplicar.'
          '\n[ 3 ] Maior.'
          '\n[ 4 ] Novos Números.'
          '\n[ 5 ] Sair do programa.')
    option = int(input('\033[31m>>>> Qual sua escolha:\033[30m '))
    if option == 1:
        soma = n1 + n2
        print('O resultado de {} + {} é {}'.format(n1, n2, soma))
    elif option == 2:
        multiplication = n1 * n2
        print('O resultado de {} X {} é {}'.format(n1, n2, multiplication))
    elif option == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n1))
        else:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n2))
    elif option == 4:
        print('\033[1;33mInforme os números novamente:')
        n1 = int(input('\033[0;30mInsira um número: '))
        n2 = int(input('Insira outro número: '))
    elif option == 5:
        print('\033[0;30mAté mais.')
    else:
        print('\033[31mOpção invalida.')
    print('\033[31m-\033[33m='*20)
print('\033[30mFinalizando o programa...')
sleep(3)
