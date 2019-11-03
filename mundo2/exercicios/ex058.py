from random import randrange
palpite = int(input('Chute o número que o PC escolheu aleatoriamente entre 0 e 10:\n'))
i = 1
pc = randrange(0, 11)
while palpite != pc:
    palpite = int(input('Você errou! Tente novamente:\n'))
    i += 1
print('Você acertou! Foram necessários {} palpites até você conseguir.'.format(i))