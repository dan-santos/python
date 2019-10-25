ano = int(input("Digite um ano: "))
if(ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print("{} é bisexto".format(ano))
else:
    print("{} não é bisexto".format(ano))