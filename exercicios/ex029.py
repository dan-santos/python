vel = int(input("Velocidade (em KM/H) do carro: "))
if vel > 80:
    print("Você foi multado em {}R$ por ultrapassar em {}Km/h a velocidade máxima permitida".format((vel-80)*7, vel-80))