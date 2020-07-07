total = TotMaiorQueMil = MenorValor = contador = 0
NomeMenorValor = ''
while True:
    print('=-'*25)
    print('{:^50}'.format('LEITOR DE PRODUTOS'))
    print('=-'*25)
    nome = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: '))
    contador += 1
    if contador == 1 or valor <= MenorValor:
        MenorValor = valor
        NomeMenorValor = nome
    total += valor  # Calculando o total gasto
    if valor > 1000:
        TotMaiorQueMil += 1 
    option = ' '
    while option not in 'SN':
        option = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if option == 'N':
        break
print(f'O total Gasto foi R${total:.2f}.')
print(f'Temos {TotMaiorQueMil} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {NomeMenorValor} que custa R${MenorValor:.2f}')
