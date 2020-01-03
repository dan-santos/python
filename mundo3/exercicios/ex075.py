valores = (int(input('Digite um valor')),
           int(input('Digite um valor')),
           int(input('Digite um valor')),
           int(input('Digite um valor')))

print(valores.count(9))
if valores.count(3) > 0:
    print(valores.index(3))
for nr in valores:
    if nr % 2 == 0:
        print(nr)