lista = []
for i in range(5):
    nr = int(input('Digite o {}º valor: '.format(i+1)))
    if i == 0:
        lista.append(nr)
    else:
        if lista[len(lista)-1] < nr:
            lista.insert(len(lista)-1, nr)
        else:
            lista.append(nr)

print(lista)