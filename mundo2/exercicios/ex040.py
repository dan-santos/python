n1 = int(input("Nota 1 [0 a 10]: "))
n2 = int(input("Nota 2 [0 a 10]: "))

med = (n1 + n2) / 2

if med >= 7:
    print('APROVADO')
elif med < 5:
    print('REPROVADO')
else:
    print('RECUPERAÇÃO')