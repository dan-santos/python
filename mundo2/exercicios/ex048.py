somatorio = 0
for i in range(1, 501):
    if i%2 != 0:
        if i%3 == 0:
            somatorio += i

print("Soma de números ímpares múltiplos de três no intervalo fechado [1,500]: {}".format(somatorio))