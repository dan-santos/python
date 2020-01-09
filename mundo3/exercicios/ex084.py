galera = list()
pessoa = list()
maisPesado = list()
maisLeve = list()
menorPeso = maiorPeso = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa)
    if len(maisPesado) == 0:
        maisPesado.append(pessoa[0])
        maisLeve.append(pessoa[0])
        maiorPeso = menorPeso = pessoa[1]
    else:
        if pessoa[1] > maiorPeso:
            maisPesado.clear()
            maisPesado.append(pessoa[0])
            maiorPeso = pessoa[1]
        elif pessoa[1] == maiorPeso:
            maisPesado.append(pessoa[0])

        if pessoa[1] < menorPeso:
            maisLeve.clear()
            maisLeve.append(pessoa[0])
            menorPeso = pessoa[1]
        elif pessoa[1] == menorPeso:
            maisLeve.append(pessoa[0])
    pessoa.clear()
    resposta = str(input('Deseja inserir mais pessoas? [Y/N]'))
    if resposta in 'Nn':
        break

print(len(galera), ' pessoas cadastradas')
print(f'As pessoas mais pesadas são {maisPesado} com {maiorPeso}Kg')
print(f'As pessoas mais leves são {maisLeve} com {menorPeso}Kg')