#help(comando desejado para obter documentação do python console)
#elemDesejado.__doc__ = é parecido com o help, mas possui alguma diferenças

#docstrings = documentação das funções criadas pelo programador
#equivalente ao javadoc

def contador(i, f, p):
    """
    Faz a contagem e mostra na tela
    :param i: início
    :param f: fim
    :param p: passo da contagem
    :return: sem retorno
    -> Autor: Daniel
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)
#help(contador)
x = 0 #global
def somar(a, b, c = 0): #ao atribuir um valor no próprio construtor
    #se está definindo um parâmetro OPCIONAL, no qual o user pode ou não
    #atualizar com algum valor. uma def pode ser composta somente por parametros opcionais
    #x = a+b+c #variável local
    global x
    x = a+b+c
    return x #retorno da função

print(somar(1, 2))
