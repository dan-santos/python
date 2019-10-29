soma = 0
for i in range(0, 6):
    nr = int(input('Digite um número inteiro: '))
    if nr%2 == 0:
        soma += nr

print('Somatório de todos os valores pares: {}'.format(soma))