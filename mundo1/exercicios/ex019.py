from random import randrange
nomes = []
for i in range(4):
    nomes.append(str(input("Digite o nome dx {}º alunx: ".format(i+1))))
print("X alunx sorteadx foi {}".format(nomes[randrange(0, 4)]))