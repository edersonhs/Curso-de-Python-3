nome = []
idade = []
sexo = []
SomaIdade = 0
MenosDe20 = 0
IdadeDoMaisVelho = 0
NomeDoMaisVelho = ''
for c in range(0, 4):
    nome += [str(input('Insira o nome da {}ª pessoa: '.format(c + 1))).strip().capitalize()]
    idade += [int(input('Insira a idade da {}ª pessoa: '.format(c + 1)))]
    sexo += [str(input('Insira o sexo da {}ª pessoa [F/M]: '.format(c + 1))).strip().lower()]
    print('=-' * 40)
    # Calculando a média de idade do grupo
    SomaIdade += idade[c]
    # Verificando o nome do homem mais velho
    if c == 0:
        IdadeDoMaisVelho = idade[c]
    else:
        if sexo[c] == 'm' and idade[c] > IdadeDoMaisVelho:
            IdadeDoMaisVelho = idade[c]
            NomeDoMaisVelho = nome[c]
    # Verificando quantas mulheres tem menos de 20 anos
    if sexo[c] == 'f' and idade[c] < 20:
        MenosDe20 += 1
print('A media de idade do grupe é de: {} anos.'.format(SomaIdade / 4))
print('O Homem mais velho tem {} anos e se chama {}.'.format(IdadeDoMaisVelho, NomeDoMaisVelho))
print('Dentre os 4 elementos, há {} mulher(es) com menos de 20 anos.'.format(MenosDe20))
