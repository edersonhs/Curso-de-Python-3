n1 = int(input('\033[1;35mInsira o primeiro número: '))
n2 = int(input('\033[1;35mInsira o segundo número: '))

if n1 > n2:
    print('\033[1;30mO primeiro valor({}) é o maior.'.format(n1))
elif n1 < n2:
    print('\033[1;30mO segundo valor({}) é o maior.'.format(n2))
else:
    print('\033[1;30mNão existe valor maior. Os dois são iguais.')