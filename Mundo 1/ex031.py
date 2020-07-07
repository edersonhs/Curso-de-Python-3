# Calcula valor da passagem.

print('\033[1;35m-\033[1;36m=' * 30)
distancia = int(input('\033[1;36mQual a distância da viagem? '))
print('\033[1;35m-\033[1;36m=' * 30)
if distancia <= 200:
    passagem = distancia * 0.50
    print('\033[1;35mO valor da passagem para uma viagem de \033[1;31m{}Km \033[1;35mé de \033[1;31mR${:.2f}\033[1;30m.'.format(distancia, passagem))
else:
    passagem = distancia * 0.45
    print('\033[1;34mO valor da passagem para uma viagem de \033[1;31m{}Km \033[1;34mé de \033[1;31mR${:.2f}\033[1;34m.'.format(distancia, passagem))
print('\033[1;30mTenha uma boa viagem!')
