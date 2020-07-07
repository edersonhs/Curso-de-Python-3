count = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('~'*38)
    if n < 0:
        break
    else:
        while True:
            if count <= 10:
                print(f'\t\t{n} x {count:>2} = {n * count}')
                count += 1
            else:
                break
    count = 1
    print('~'*38)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')



