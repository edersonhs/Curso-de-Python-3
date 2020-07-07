ListaNum = list()

while True:
    numero = int(input('Digite um número: '))
    if numero not in ListaNum:
        ListaNum.append(numero)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar...')
    option = str(input('Quer continuar? [S/N] ')).strip().upper()
    if option == 'N':
        break
ListaNum.sort()
print(f'Você digitou os valores {ListaNum}')
