# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionario se por acaso o CTPS (Cateira de trabalho de previdencia social)for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.

# 35 anos de contribuição pra se aposentar.

from datetime import datetime   # Ano atual

agora = datetime.now()
anoAtual = agora.year
pessoa = dict()

pessoa['nome'] = str(input('Nome: ')).strip().title()
anoNascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = anoAtual - anoNascimento
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
    pessoa['ctps'] = ctps
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Sálario: '))
    tempoContribuicao = anoAtual - pessoa['contratação']
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - tempoContribuicao)

print('=-' * 30)
print(f"Seu nome é: {pessoa['nome']}.")
print(f"Você tem {pessoa['idade']} anos.")
if ctps != 0:
    print(f"Sua carteira de trabalho é: {pessoa['ctps']}.")
    print(f"Você foi contratado em {pessoa['contratação']}.")
    print(f"Seu sálario é: R${pessoa['salário']}.")
    print(f"Você se aposentará com {pessoa['aposentadoria']} anos.")
else:
    print('Você não possui Carteira de Trabalho.')
