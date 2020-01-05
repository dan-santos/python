from random import randint
jogos = list()
numeros = list()

numJogos = int(input('Quantos jogos serão gerados? '))

for i in range(numJogos):
    for j in range(6):
        nr = randint(1, 60)
        while nr in numeros:
            nr = randint(1, 60)
        numeros.append(nr)
    jogos.append(numeros[:])
    numeros.clear()
    print(jogos[i])