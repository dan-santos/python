nr = str(input("DIgite um número entre 0 e 9999: "))
tam = len(nr)

for i in range(tam):
    print("{}º número: {}".format(i+1, nr[i]))


