def leiaDinheiro(msg):
    valido = False
    while not valido:
        dinheiro = str(input(msg)).replace(',', '.').strip()
        if dinheiro.isalpha() or dinheiro == '':
            print(f'ERRO: "{dinheiro}" é um preço inválido!')
        else:
            valido = True
            return float(dinheiro)
