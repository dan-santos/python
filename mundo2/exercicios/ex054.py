nasc = []
maiores = 0
for i in range(0, 7):
    nasc.append(int(input('Digite a data de nascimento da {}ª pessoa: '.format(i+1))))
    if 2019-nasc[i] < 21:
        maiores += maiores

print('Quantidade de pessoas que não são maiores de idade: {}'.format(maiores))