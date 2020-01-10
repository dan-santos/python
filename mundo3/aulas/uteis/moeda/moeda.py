def aumentar(num, porc):
    """
    Aumenta em determinada porcentagem o valor passado
    como parâmetro
    :param num: numero a ser aumentado
    :param porc: porcentagem de aumento
    :return: float
    """
    return num+((num*porc)/100)

def diminuir(num, porc):
    """
    Diminui em determinada porcentagem o valor passado
    como parâmetro
    :param num: numero a ser reduzido
    :param porc: porcentagem de redução
    :return: float
    """
    return num-((num*porc)/100)

def dobro(num):
    """
    Calcula o dobro do valor passado
    :return: type(num)
    """
    return num*2

def metade(num):
    """
    Calcula a metade do valor passado
    :param num: número a ser divido
    :return: type(num)
    """
    return num/2

def resumo(p, aumento, reducao):
    """
    Faz um resumo contendo todas as funções do módulo numa só saída
    :param p: preço analisado
    :param aumento: porcentagem de aumento
    :param reducao: porcentagem de reducação
    :return: string do resumo
    """

    resumo = '-'*25
    resumo += '\n     RESUMO DO VALOR    \n'
    resumo += '-'*25
    resumo += f'\nPreço analisado: {p}'
    resumo += f'\nDobro do preço: {dobro(p)}'
    resumo += f'\nMetade do preço: {metade(p)}'
    resumo += f'\n{aumento}% de aumento: {aumentar(p, aumento)}'
    resumo += f'\n{reducao}% de redução: {diminuir(p, reducao)}\n'
    resumo += '-' * 25

    return resumo