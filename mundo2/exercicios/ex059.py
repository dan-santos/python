opc = 4

def menu():
    opcao = int(input('[1] - Somar\n'
          '[2] - Multiplicar\n'
          '[3] - Maior\n'
          '[4] - Novos números\n'
          '[5] - Sair do programa\n'))
    return opcao


while opc:
    num1 = int(input('Digite o primeiro valor:\n'))
    num2 = int(input('Digite o segundo valor:\n'))
    opc = menu()
    if opc == 1:
        print(int(num1+num2))
    elif opc == 2:
        print(int(num1*num2))
    elif opc == 3:
        if num1 >= num2:
            print(num1)
        else:
            print(num2)
    elif opc == 4:
        opc = menu()
    elif opc == 5:
        break






