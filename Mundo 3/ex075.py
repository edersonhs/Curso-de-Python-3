numeros = (int(input('Insira o primeiro número: ')), int(input('Insira o segundo número: ')),
           int(input('Insira o terceiro número: ')), int(input('Insira o quarto número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if numeros.count(3) != 0:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n}, ', end='')
