n = int(input('\033[1;30mInsira um número inteiro: '))

if n % 2 == 0:
    print('\033[1;32mO número {} é Par.'.format(n))
else:
    print('\033[1;34mO número {} é Impar.'.format(n))