print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
cedula = 50
totalCedula = 0
while True:
    if total >= cedula:     # Verifica se o valor é maior ou igual a cédula (Começando em 50)
        total -= cedula     # Subtrai a cédula do total
        totalCedula += 1    # Incrementa um no contador de cédulas
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        totalCedula = 0     # Zerando o contador de cédulas
        # Definindo a proxima cédula
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        # Definindo final do laço
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao banco CEV! Tenha um bom dia!')
