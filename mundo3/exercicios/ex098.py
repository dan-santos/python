from time import sleep
def lin():
    print('-='*30)


def contIni(ini, fim, pas):
    if pas < 0: #alterando valor do passo para positivo só para printar
        print(f'Contagem de {ini} até {fim} de {-pas} em {-pas}')
    else:
        print(f'Contagem de {ini} até {fim} de {pas} em {pas}')

    fim += pas  # impedindo que o for pare antes de chegar no fim
    for i in range(ini, fim, pas):
        print(f'{i}', end=' ')
        sleep(0.5)
    print('FIM!', end='\n')


def contador(ini, fim, pas):
    lin()
    if pas == 0:  # pas passa a valer 1
        pas = 1
    if ini < fim:
        if pas < 0:
            pas = -pas
    elif ini > fim:
        if pas > 0:
            pas = -pas
    contIni(ini, fim, pas)


contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))