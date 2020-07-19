# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGRATÓRIO nas eleições.


def voto(anoNascimento):
    from datetime import datetime
    anoAtual = datetime.now().year
    idade = anoAtual - anoNascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    if idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print(voto(2003))
