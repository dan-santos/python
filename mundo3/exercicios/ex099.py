from random import randint
from time import sleep
def maior(*num):
    tam = len(num)
    maior = num[0]
    for elem in num:
        if elem > maior:
            maior = elem
    print('-='*30)
    print('Analisando valores passados...')
    print(f'{num} foram passados, resultando em {tam} valores')
    print(f'O maior valor informado foi {maior}')


for i in range(5):
    maior(randint(0, 42), randint(0, 42), randint(0, 42), randint(0, 42),
          randint(0, 42), randint(0, 42), randint(0, 42), randint(0, 42))
    sleep(1)