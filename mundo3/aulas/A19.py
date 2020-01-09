filme = dict()
filme = {'Título': 'Star Wars',
         'Ano': '1977',
         'Diretor': 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items()) #Cada item = (coluna, valor)

for key, valor in filme.items():
    print(f'O {key} é {valor}')

filme2 = {'Título':'Matrix',
          'Ano':'1999',
          'Diretor':'Wachowski'}
del filme2['Diretor']
filme2['Avaliação'] = '5 estrelas' #Não é preciso dar um append para criar novas keys/values
for k in filme2.values():
    print(k)

locadora = list()
locadora.append(filme)
locadora.append(filme2)

print(locadora)
print(locadora[1]['Título'])

print('-'*30)

estado = dict()
brasil = list()
for c in range(3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['nome'] = str(input('Nome do estado: '))
    brasil.append(estado.copy()) # equivalente ao estado{:}
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()