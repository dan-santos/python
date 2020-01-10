def leia(texto):
    """
    → Função para leitura e validação de um valor monetário.
    :param texto: a ser apresentado para o usuário
    :return: um valor do tipo float
    """

    while True:

        valor = str(input(texto)).strip().replace(',', '.')

        if valor.replace('.', '').isnumeric():
            break

        print(f'\033[1;31mO valor digitado \"{valor}\", é um preço inválido!\033[m')