from datetime import date
from time import sleep
import emoji
print('\033[32;1m')
print('''
 __ __ _ _   _ _____ __  _____   __  ___ ___ ______ _  _ _ _____ __ __ ___ __  _ _____  
|  V  | | | | |_   _/  \| _ \ `v' / | _ \ __/ _/ _ \ || | |_   _|  V  | __|  \| |_   _| 
| \_/ | | |_| | | || /\ | v /`. .'  | v / _| \_| v / \/ | | | | | \_/ | _|| | ' | | |   
|_| |_|_|___|_| |_||_||_|_|_\ !_!   |_|_\___\__/_|_\\__/|_| |_| |_| |_|___|_|\__| |_|   
''')
sexo = str(input('\033[1;30mQual seu sexo?'
                 '\n\033[1;36m[ M ] Homen.'
                 '\n[ F ] Mulher.'
                 '\n\033[1;30mSua escolha: ')).upper().strip()
if sexo == 'F':
    escolha = str(input('\nO alistamento não é obrigatorio para mulheres. Deseja continuar? '
                        '\n\033[1;36m[ S ] Sim'
                        '\n[ N ] Não'
                        '\n\033[1;30mSua escolha: ')).upper().strip()
    if escolha == 'S':
        print(emoji.emojize('\033[33;1mQue bom :smiley:. Processando...', use_aliases=True))
        sleep(3)
    elif escolha == 'N':
        print(emoji.emojize('\033[1;33mQue pena... :disappointed:', use_aliases=True))
        sleep(3)
        exit()
AnoNascimento = int(input('\n\033[30;1mQual sua data de nascimento? '))
idade = date.today().year - AnoNascimento
alistamento = (18 - idade) + date.today().year
if idade < 18:
    print('\033[1;34mVocê ainda tem {} anos. Por ser menor de 18 anos, você deve comparecer na junta militar em {}, quando terá 18 anos.'.format(idade, alistamento))
elif idade > 18:
    print('\033[31;1mVocê já tem {} anos e deveria ter comparecido na junta militar para alistamento assim que chegou aos 18 anos, em {}.'.format(idade, alistamento))
    print('Compareça o quanto antes na junta militar mais próxima, visto que esta {} anos atrasado.'.format(date.today().year - alistamento))
else:
    print('\033[1;32mVocê tem 18 anos e esta na hora de se alistar. Procure a junta militar mais próxima.')
