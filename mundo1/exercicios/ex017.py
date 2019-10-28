from math import pow
from math import sqrt
ca = float(input("Insira o valor do cateto adjacente: "))
co = float(input("Insira o valor do cateto oposto: "))
hi = pow(ca, 2)+pow(co, 2)
hi = sqrt(hi)
print("A hipotenusa vale: {}".format(hi))