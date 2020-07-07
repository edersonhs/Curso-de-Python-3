n1 = int(input('\033[1;35mDigite um número: '))
n2 = int(input('\033[1;34mDigite um segundo número: '))
n3 = int(input('\033[1;33mDigite um terceiro número: '))
# Verificando quem é maior.
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
# Verificando quem é menor.
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\n\033[1;36mO maior valor digitado foi {}.'.format(maior))
print('\033[1;34mO menor valor digitado foi {}.'.format(menor))
