lista = []
continua = 'y'
while continua == 'y':
    lista.append(int(input('Digite um valor inteiro: ')))
    continua = str(input('Deseja inserir mais algum valor? [y/n]: '))

print(len(lista))
print(sorted(lista, reverse=True))
if 5 in lista:
    print('O 5 foi digitado {} vezes.'.format(lista.count(5)))
else:
    print('O 5 não foi digitado nenhuma vez')