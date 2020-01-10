def leiaInt(numero):
    if numero.isdigit():
        return True
    else:
        return False

print(leiaInt(input('Digite um número inteiro: ')))