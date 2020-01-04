lista = []
for i in range(5):
    nr = int(input('Digite um valor inteiro: '))
    if lista.count(nr) < 1: #analisando valores repetidos
        lista.append(nr)

print(sorted(lista))