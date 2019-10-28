nr = []
maior = 0
menor = 0

for i in range(0, 3):
    nr.append(float(input("Digite o {} número: ".format(i+1))))
    if i == 0:
        maior = nr[i]
        menor = nr[i]
    else:
        if nr[i] > maior:
            maior = nr[i]
        if nr[i] < menor:
            menor = nr[i]

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))