# Faça um algoritimo que leia o sálario de um funcionario e mostre o seu novo salário, com 15% de aumento.

salario = float(input('Insira o seu salario atual: '))
aumento = (15 * salario) / 100

print('Seu salario ({:.2f}R$) com um aumento de 15% ({:.2f}R$) fica: {:.2f}R$.'.format(salario, aumento, salario + aumento))
