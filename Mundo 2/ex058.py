from random import randint
attempts = 1
computer = randint(0, 10)
player = int(input('Vou pensar em um número entre 0 e 10, tente adivinhar...\nEm qual número eu pensei? '))
while player != computer:
    if player < computer:
        player = int(input('Mais... Tente de novo.\nEm qual número eu pensei? '.format(computer)))
    else:
        player = int(input('Menos... Tente de novo.\nEm qual número eu pensei? '.format(computer)))
    attempts += 1
print('PARABÉNS! Você acertou com {} tentativas! Eu pensei no número {}.'.format(attempts, computer))
