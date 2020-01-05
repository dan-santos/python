vert = [[], [], []]
hori = list()
pares = soma = maior = 0
for i in range(3):
    for j in range(3):
        hori.append(int(input('Digite um número: ')))
        if hori[j] % 2 == 0:
            pares += hori[j]
    soma += hori[2]
    vert[i].append(hori[:])
    if i == 1:
        for nr in hori:
            if nr > maior:
                maior = nr
    hori.clear()

for i in range(3):
    print(vert[i])

print(pares)
print(soma)
print(maior)