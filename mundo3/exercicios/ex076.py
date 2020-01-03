tabela = 'Notebook', 3.222, 'Celular', 1.230, 'PC', 4500

for i in tabela:
    print(f'{tabela[tabela.index(i):tabela.index(i)+2]}\n')

