from random import randint
from time import sleep
def sorteia():
    print('Sorteando números ...')
    numeros = list()
    for i in range(5):
        numeros.append(randint(0, 100))
        print(numeros[i], end=' ')
        sleep(1)
    print('\nSorteio terminado')
    print('-='*30)
    somaPar(numeros)

def somaPar(lista):
    print('Iniciando soma de números pares ...')
    soma = 0
    print('Números pares da lista: ')
    for i in lista:
        if i % 2 == 0:
            print(f'{i}', end=' ')
            sleep(1)
            soma += i
    print(f'\nA soma dos valores acima é {soma}')

sorteia()