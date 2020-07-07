salario = float(input('Informe o salário  do funcionário:'))

if salario > 1250:
    aumento = salario + 10 * salario / 100
else:
   aumento = salario + 15 * salario / 100
print('O funcionário recebia R${:.2f} e passará a receber R${:.2f}'.format(salario, aumento))
