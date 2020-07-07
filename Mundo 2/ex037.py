# Conversor de decimal para Binario/Hexadecilmal/Octal.
n = int(input('\033[1;33mInsira um número inteiro: '))
print('Escoha a base para conversão:')
print('\033[1;34m[ 1 ] Converter para Binário.')
print('[ 2 ] converter para Octal.')
print('[ 3 ] Converter para Hexadecimal.')
base = int(input('\033[1;33mInsira a opção desejada: \033[1;36m'))
if base == 1:
    binario = str(bin(n))
    print('O número digitado foi {} e convertido para binario fica {}.'.format(n, binario[2:len(binario)])) # Era possivel tbm ".format(n, bin(n)[2:])"
elif base == 2:
    octal = str(oct(n))
    print('O número digitado foi {} e convertido para octal fica {}.'.format(n, octal[2:len(octal)]))
elif base == 3:
    hexadecimal = str(hex(n))
    print('O número digitado foi {} e convertido para Hexadecimal fica {}.'.format(n, hexadecimal[2:len(hexadecimal)]))
else:
    print('Opção invalida. Tente novamente.')