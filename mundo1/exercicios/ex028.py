from random import randrange
nr = int(input("Adivinhe o número que o computador pensou [0, 5]"))
num = randrange(0, 5)
if num == nr:
    print("Você adivinhou!")
else:
    print("Você não adivinhou :( O número certo é {}".format(num))