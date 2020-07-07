aluno = list()
nome = list()
notas = list()
media = list()
alunos = list()

# Cadastrando Aluno
print('-=' * 40)
print(f'{" GESTÃO DE PROVAS E ALUNOS ":=^80}')
print('-=' * 40)
while True:
    nome.append(str(input('Nome: ')).strip().title())
    c = 0
    SomaNota = 0
    while c != 2:
        nota = float(input(f'Nota {c+1}: '))
        if 0 < nota <= 10:
            notas.append(nota)
            SomaNota += nota
            c += 1
        else:
            print('Nota invalida! Tente novamente.')
    aluno.append(nome[:])
    aluno.append(notas[:])
    media.append(SomaNota / 2)
    aluno.append(media[:])
    alunos.append(aluno[:])
    aluno.clear()
    nome.clear()
    notas.clear()
    media.clear()
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if 'N' in opcao:
        break

# Imprimindo boletim
print('-=' * 40)
print('No. NOME           MÉDIA')
print('-' * 30)
for i, l in enumerate(alunos):
    print(f'{i+1:<2}', f'{l[0][0]:<16}', f'{l[2][0]}')
print('-=' * 40)

# Verificar notas individuais
while True:
        idAluno = int(input('Mostrar Notas de qual Aluno? (999 interrompe): '))
        if idAluno == 999:
            break
        if idAluno <= len(alunos):
            print(f'Notas de {alunos[idAluno-1][0][0]} são {alunos[idAluno-1][1]}.')
        else:
            print('Aluno inexistente! Tente novamente.')
        print('-' * 80)
print('<<<< VOLTE SEMPRE >>>>')

'''
# Exmplo diferente de lista composta mais eficiente
ficha = list()
alunos = list()

while True:
    nome = str(input('Nome:').title().strip())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    alunos.append(ficha[:])
    opcao = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if 'N' in opcao:
        break
    ficha.clear()
print(alunos)
'''
