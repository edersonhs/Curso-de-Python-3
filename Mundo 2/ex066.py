count = soma = 0
while True:
    n = int(input('Insira um número (999 para parar): '))
    if n == 999:
        break
    else:
        count += 1
        soma += n
print(f'Foram digitados {count} números e a soma deles é {soma}')
