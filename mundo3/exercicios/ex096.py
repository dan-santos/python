def cabecalho():
    print('  Calcular área de terreno')
    print('-'*28)


def area(altura, comprimento):
    print(f'A área do terreno é igual a {altura*comprimento}m²')

cabecalho()
area(float(input('Largura: ')), float(input('Comprimento: ')))