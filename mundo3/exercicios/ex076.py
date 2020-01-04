tabela = 'Notebook', 3.222, 'Celular', 1.230, 'PC', 4.500

for i in range(len(tabela)):
    if i%2==0:
        print(f'{tabela[i]:.<30}', end='')
    else:
        print(f'R${tabela[i]:>.3f}')
