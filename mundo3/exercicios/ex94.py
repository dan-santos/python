lista = []

while True:
    dic = {"Nome": str(input('Nome: ')).strip().capitalize(),
          "Sexo": str(input('Sexo: (M/F)')).strip().capitalize().upper()[0],
          "Idade": int(input('Idade: '))}

    lista += [dic]

    flag = str(input('Continuar? (S/N)')).strip().lower()[0]
    if flag == 'n':
        break

media = [lista[i]["Idade"] for i in range(0, len(lista))]
media = (sum(media)) / (len(media))
mulheres = [lista[i]["Nome"] if lista[i]["Sexo"] == 'F' else '' for i in range(0, len(lista))]
mulheres = [x for x in mulheres if x != '']
acima = [lista[i]["Idade"] if lista[i]["Idade"] > media else '' for i in range(0, len(lista))]
acima = [x for x in acima if x != '']  ## Apenas para remover os espaços em branco
acimanome = [lista[i]["Nome"] if lista[i]["Idade"] > media else '' for i in range(0, len(lista))]
acimanome = [x for x in acimanome if x != '']
acima = [f'{acimanome[i]}: {acima[i]} 'for i in range(0, len(acima))]

print('\n', '*'*15, 'RESULTADOS', '*'*15)
print(f'Total de pessoas: {len(lista)}'
      f'\nMédia de idade: {media:.2f} anos'
      f'\nHá {len(acima)} pessoas com idade acima da média: {acima}'
      f'\nHá {len(mulheres)} mulheres do grupo: {mulheres}')