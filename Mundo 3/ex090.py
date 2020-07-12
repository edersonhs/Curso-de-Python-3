# Faca um programa que leia nome e média de um aluno, guardando também a situação (7 or + == aprovado) em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome'] = str(input('Nome: ')).title().strip()
media = float(input(f'Média de {aluno["nome"]}: '))

if media >= 7:
    aluno['situaçao'] = 'APROVADO'
else:
    aluno['situaçao'] = 'REPROVADO'

print('=-' * 30)
print(f'Nome: {aluno["nome"]}')
print(f'Situação: {aluno["situaçao"]}')
