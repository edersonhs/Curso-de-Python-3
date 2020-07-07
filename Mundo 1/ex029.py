# Radar elêtronico
velocidade = int(input('\033[1;35mQual a velocidade atual do carro: '))

if velocidade > 80:
    print('\033[1;31mMULTADO! \033[1;30mVocê ultrapassou o limite de velocidade permitido, que é de \033[1;31m80Km/h! '
          '\033[1;30mVocê deve pagar uma multa de \033[1;31mR${}\033[1;30m!'.format((velocidade - 80) * 7))

print('\033[1;33mTenha um bom dia! Dirija com segurança!')
