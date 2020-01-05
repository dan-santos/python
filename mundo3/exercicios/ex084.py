galera = list()
pessoa = list()
maisPesado = list()
maisLeve = list()
pesoMaior = 0
pesoMenor = 1000000
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if pessoa[1] >= pesoMaior:
        if pessoa[1] != pesoMaior and len(maisPesado) > 0:
            maisPesado.pop()
        pesoMaior = pessoa[1]
        maisPesado.append(pessoa[0])
    if pessoa[1] <= pesoMenor:
        if pessoa[1] != pesoMenor and len(maisLeve) > 0:
            maisLeve.pop()
        pesoMenor = pessoa[1]
        maisLeve.append(pessoa[0])
    galera.append(pessoa[:])
    pessoa.clear()
    opt = str(input('Quer inserir mais uma pessoa? [Y/N]'))
    if 'N' in opt or 'n' in opt:
        break
print(f'{len(galera)} pessoas cadastradas')
print(f'O(s) mais pesado(s) ({pesoMaior}) é/são {maisPesado}')
print(f'O(s) mais leve(s) ({pesoMenor}) é/são {maisLeve}')