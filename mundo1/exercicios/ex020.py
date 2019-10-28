import random
nomes = []
for i in range(4):
    nomes.append(input("Digite o nome do {} aluno: ".format(i+1)))
random.shuffle(nomes)
print(nomes)