lista = []
continua = 'y'
while continua == 'y':
    lista.append(int(input('Digite um valor inteiro: ')))
    continua = str(input('Deseja inserir mais algum valor? [y/n]: '))

pares = []
impares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(lista)
print(pares)
print(impares)