nr = int(input('Insira um número inteiro positivo: '))
div = 0
if nr != 2:
    for i in range(1, nr+1):
        if nr % i == 0:
            div += 1

    if div == 2:
        print('{} é primo!'.format(nr))
    else:
        print('{} não é primo!'.format(nr))
else:
    print('2 não é primo.')

