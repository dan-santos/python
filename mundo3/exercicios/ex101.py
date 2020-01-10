from datetime import date
def voto(anoNasc):
    idade = date.today().year - anoNasc
    if idade < 17:
        return 'NEGADO'
    elif idade == 17 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓTIO'


print(f'VOTO {voto(int(input("Insira seu ano de nascimento: ")))}')