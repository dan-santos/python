from random import randint
resultados = dict()
vencedor = 0
index = 1
for i in range(4):
    nr = randint(1, 6)
    resultados[str(f'valorDado{i}')] = nr
    if i == 0:
        vencedor = nr
    else:
        if nr > vencedor:
            vencedor = nr
            index = i
        elif nr == vencedor:
            index = str(f'{index} e {i}')

print(sorted(resultados.values(), reverse=True))
print(f'O {index}o a jogar o dado ganhou')