expressao = str(input('Digite a expressão: '))
pilha = list()

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()     # Apaga o ultimo elemento da lista
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão esta válida!')
else:
    print('Sua expressão está errada!')
