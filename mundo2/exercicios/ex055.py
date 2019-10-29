pesos = []
maior = menor = 0
for i in range(0, 5):
    pesos.append(float(input('Digite o peso, em Kg, da {}ª pessoa: '.format(i+1))))
    if i == 0:
        maior = pesos[i]
        menor = pesos[i]
    else:
        if pesos[i] > maior:
            maior = pesos[i]
        if pesos[i] < menor:
            menor = pesos[i]

print('Maior peso: {}\nMenor peso: {}'.format(maior, menor))