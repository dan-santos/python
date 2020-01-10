def leiaInt(numero):
    try:
        if numero.isdigit():
            return True
    except:
        return 'Tipo inválido'

def leiaFloat(numero):
    try:
        if numero.isdecimal():
            return True
    except:
        return 'Tipo inválido'

print(leiaInt(input('Digite um número inteiro: ')))
print(leiaFloat(input('Digite um número decimal: ')))