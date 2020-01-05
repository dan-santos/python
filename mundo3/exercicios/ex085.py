numeros = [[], []]

for i in range(7):
    nr = int(input('Digite um número inteiro: '))
    if nr % 2 == 0:
        numeros[0].append(nr)
    else:
        numeros[1].append(nr)

print(f'{sorted(numeros[0])} / {sorted(numeros[1])}')