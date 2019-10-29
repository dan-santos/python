nr = int(input('Digite um número para a tabuada ser mostrada: '))

for i in range(1, 11):
    print('{}x{}={}'.format(i,nr,i*nr))