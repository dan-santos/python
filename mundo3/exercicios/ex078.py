lista = []
maior = 0
menor = 0
for i in range (5):
    lista.append(input('Digite um número: '))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

print('Maior valor {} na posição {} da lista'.format(maior, lista.index(maior)))
print('Menor valor {} na posição {} da lista'.format(menor, lista.index(menor)))