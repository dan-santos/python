vert = [[], [], []]
hori = list()

for i in range(3):
    for j in range(3):
        hori.append(int(input('Digite um número: ')))
    vert[i].append(hori[:])
    hori.clear()

for i in range(3):
    print(vert[i])