from time import sleep
print('\033[0;30m-=' * 40)
print('{:^60}'.format('\033[1;33mTermos de uma Pregressão Aritimética (Com While e limite definido pelo usúario)\033[0;30m'))
print('-=' * 40)
inicio = int(input('Insira o primeiro termo: '))
intervalo = int(input('Insira a razão: '))
MenuCont = 1
qtdTermos = 10
qtdRepeticoes = 0
while MenuCont != 0:
    c = 1
    while c <= qtdTermos:
        print('\033[1;31m{} \033[1;33m-> '.format(inicio) if c < qtdTermos else '\033[1;31m{}'.format(inicio), end='')
        inicio += intervalo
        c += 1
        qtdRepeticoes += 1
    escolha = str(input('\n\033[0;30mDeseja continuar? [S/N] ')).upper().strip()[0]
    if escolha == 'S':
        qtdTermos = int(input('Informe a quantidade de termos que deseja vizualizar: '))
    else:
        MenuCont = 0
        print('Progressão finalizada com {} temos mostrados.'.format(qtdRepeticoes))
        sleep(3)
