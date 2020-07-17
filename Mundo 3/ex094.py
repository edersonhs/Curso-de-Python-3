# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:

#       A) Quantas pessoas foram cadastradas.
#       B) A média de idade do grupo.
#       C) Uma lista com todas as mulheres.
#       D) Uma lista com todas as pessoas com idade acima da média

pessoa = dict()
pessoas = list()
mulheres = list()
idadeAcimaMedia = list()
totalCadastros = 0
idadeMediaGrupo = 0
somaIdadeGrupo = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('OPÇÃO INVALIDA! Tente novamente. (S/N)')
    pessoa['idade'] = int(input('Idade: '))
    somaIdadeGrupo += pessoa['idade']

    print('=-' * 30)

    pessoas.append(pessoa.copy())

    totalCadastros += 1
    opt = input('Quer continuar (S/N)?').upper().strip()[0]
    if opt == 'N':
        break

idadeMediaGrupo = somaIdadeGrupo // totalCadastros

for c, v in enumerate(pessoas):
    if pessoas[c]['sexo'] == 'F':
        mulheres.append(pessoas[c])
    if pessoas[c]['idade'] > idadeMediaGrupo:
        idadeAcimaMedia.append(pessoas[c])

print('-=' * 30)
print(f"O grupo tem {len(pessoas)} pessoas.")
print(f"A médias de idade é de {idadeMediaGrupo} anos.")

if len(mulheres) > 0:
    print("As mulheres cadastradas foram", end=' ')
    for mulher in mulheres:
        print(mulher['nome'],end=' ')
else:
    print('Não foram cadastradas mulheres.')

if len(idadeAcimaMedia) > 0:
    print('\nLista das pessoas que estão acima da idade média: ')
    for c, v in enumerate(idadeAcimaMedia):
        print(
            f"\nNome = {idadeAcimaMedia[c]['nome']}; sexo = {idadeAcimaMedia[c]['sexo']}; idade = {idadeAcimaMedia[c]['idade']}")
else:
    print('Não existe uma idade média para o número de pessoas cadastrado.')
print(f'{"<< ENCERRADO >>":^60}')
