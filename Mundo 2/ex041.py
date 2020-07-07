from datetime import date
nasc = int(input('\033[1;30mEm que ano você nasceu? '))
idade = date.today().year - nasc
if idade <= 9:
    print('\033[1;34mVocê tem {} anos e esta na categoria MIRIN.'.format(idade))
elif (idade > 9) and (idade <= 14):
    print('\033[1;33mVocê tem {} anos e esta na categoria INFANTIL.'.format(idade))
elif (idade > 15) and (idade <= 19):
    print('\033[1;35mVocê tem {} anos e esta na categoria JUNIOR.'.format(idade))
elif (idade > 19) and (idade <= 20):
    print('\033[1;32mVocê tem {} anos e esta na categoria SÊNIOR.'.format(idade))
else:
    print('\033[1;31mVocê tem {} anos e esta na categoria MASTER.'.format(idade))
