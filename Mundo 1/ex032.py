from datetime import date
cores = {'azul': '\033[1;36m',
         'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vemelho': '\033[1;31m'}
ano = int(input('{}Que ano quer analisar? {}Insira {}0 {}para analisar o ano atual: '.format(cores['azul'], cores['limpa'], cores['verde'], cores['limpa'])))
if ano == 0:
    ano = date.today().year     # Pega a data de hoje e extrai apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}O ano {}{}{} é bissexto.'.format(cores['verde'], cores['azul'], ano, cores['verde']))
else:
    print('{}O ano {}{}{} não é bissexto{}.'.format(cores['verde'], cores['azul'], ano, cores['vemelho'], cores['verde']))
print('Fim do programa')
