pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ').strip().title()))
    dados.append(float(input('Peso: ')))
    # VERIFICANDO QUAL O MAIOR PESO DIGITADO
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    opt = str(input('Deseja continuar[S/N]? ')).strip()[0]
    if opt in 'Nn':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso:.2f}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menorpeso}KG peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print(f'[{p[0]}] ', end='')
