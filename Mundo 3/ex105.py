# Faça um programa que tenha uma função nota() que pode receber vàrias notas de alunos e vai retornar um dicionário
# com as seguintes informações:

# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

# Adicione também as DocStrings da função.


def nota(*notas, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos.
    :param situacao: Valor opcional indicando se deve ou não mostrar a situação.
    :return: Dicionário com várias informações sobre a turma.
    """
    resp = dict()
    resp['qtdNotas'] = len(notas)
    resp['maior'] = max(notas)
    resp['menor'] = min(notas)
    somaNotas = 0
    for c in notas:
        somaNotas += c  # Poderia substituir por "sum(notas)/len(notas)"
    resp['media'] = somaNotas / len(notas)
    if situacao:
        if resp['media'] < 6:
            resp['situacao'] = 'RUIM'
        elif resp['media'] == 6:
            resp['situacao'] = 'RAZOAVEL'
        else:
            resp['situacao'] = 'BOA'
    return resp


print(nota(5.5, 9.3, 10, 6.5, situacao=True))
