dias = int(input("Quantos dias o carro foi alugado? "))
km = int(input("Quantos quilômetros fotam rodados? "))

print("O valor a ser pago é {}R$".format(60*dias + 0.15*km))