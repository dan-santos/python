from random import randint
def notas(notas):
    """
    Calcula e retorna o total de notas, assim com a mais baixa,
    a mais alta, a média e a situação em forma de dicionário
    :param notas: list() com as notas
    :return: dict() com os dados acima
    """
    tam = maior = menor = media = 0
    for pos, nota in enumerate(notas):
        if pos == 0:
            maior = menor = nota
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

    tam = len(notas)
    media = sum(notas) / tam
    return {'total': tam,
            'maior': maior,
            'menor': menor,
            'media': media}

elements = list()
for i in range(10):
    elements.append(randint(0, 10))

print(notas(elements))