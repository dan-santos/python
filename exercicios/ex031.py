dist = int(input("Insira a distância, em km, da viagem: "))
if dist <= 200:
    print("O preço de uma viagem de {}Km é {}R$".format(dist, dist*0.5))
else:
    print("O preço de uma viagem de {}Km é {}R$".format(dist, dist * 0.45))