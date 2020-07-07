print('\033[1;31m-\033[1;33m=' * 65)
print('''\033[1;33m         _                 __                              __                                            __  _                    
   _____(_)___ ___  __  __/ /___ __________ _____     ____/ /__     ___  ____ ___  ____  ________  _____/ /_(_)___ ___  ____      
  / ___/ / __ `__ \/ / / / / __ `/ ___/ __ `/ __ \   / __  / _ \   / _ \/ __ `__ \/ __ \/ ___/ _ \/ ___/ __/ / __ `__ \/ __ \     
 (__  ) / / / / / / /_/ / / /_/ / /__/ /_/ / /_/ /  / /_/ /  __/  /  __/ / / / / / /_/ / /  /  __(__  ) /_/ / / / / / / /_/ /     
\033[1;31m/____/_/_/ /_/ /_/\__,_/_/\__,_/\___/\__,_/\____/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/   \___/____/\__/_/_/ /_/ /_/\____/      
                                                                               /_/                                                
''')
print('\033[1;31m-\033[1;33m=' * 65)
valor = float(input('\033[1;31mQual o valor da casa? \033[0;30mR$'))
renda = float(input('\033[1;31mQual sua renda mensal? \033[0;30mR$'))
tempo = int(input('\033[1;31mEm quantos anos pretende terminar de pagar? '))

prestacao = valor / (tempo * 12)

if prestacao > renda * 30 / 100:
    print('\033[1;33mPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} e excede 30% da sua renda mensal, portanto o emprestimo foi \033[1;31mNEGADO\033[1;33m.'.format(valor, tempo, prestacao))
else:
    print('\033[1;33mPara pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}, portanto o emprestimo pode ser \033[1;32mCONCEDIDOO\033[1;33m.'.format(valor, tempo, prestacao))
