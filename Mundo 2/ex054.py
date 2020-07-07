from datetime import date
AnoNascimento = ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty']
ano = date.today().year
MenorDeIdade = 0
MaiorDeIdade = 0
for c in range(0, 7):
    AnoNascimento[c] = int(input('Em que ano a {}ª pessoa nasceu? '.format(c + 1)).strip())
    if AnoNascimento[c] < (ano - 18):
        MaiorDeIdade += 1
    else:
        MenorDeIdade += 1
print('Menor de Idade = {}'
      '\nMaior de Idade = {}'.format(MenorDeIdade, MaiorDeIdade))
