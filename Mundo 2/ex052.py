number = int(input('Insira um número: '))
DivisionCount = 0
for c in range(1, number + 1):
    if number % c == 0:
        DivisionCount += 1
        print('\033[1;32m{}'.format(c), end=' ')     # 32 == Verde
    else:
        print('\033[1;31m{}'.format(c), end=' ')
print('\033[1;30m')
if DivisionCount == 2:
    print('\nO número {} foi divisível {} vezes\nE por isso ele \033[1;32mÉ PRIMO.'.format(number, DivisionCount))
else:
    print('\nO número {} foi divisivel {} vezes\nE por isso ele \033[1;31mNÃO É PRIMO.'.format(number, DivisionCount))