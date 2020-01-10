def fatorial(nr, show=True):
    """
    Calcula o fatorial de nr
    :param nr: nr a ser fatorado
    :param show: mostrar td o processo de multiplicação
    :return: se show=True, string. senão, int
    """
    print(show)
    texto = ''
    resultado = 1
    for i in range(nr, 0, -1):
        resultado *= i
        if show:
            if i != 1:
                texto += f'{i} x '
            else:
                texto += f'{i} = {resultado}'
    if show:
        return texto
    else:
        return resultado


print(fatorial(int(input('Digite um número para ser fatorado: ')), show=bool(input('Mostrar processo? [Enter se não] '))))
