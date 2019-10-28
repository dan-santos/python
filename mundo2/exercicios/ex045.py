from random import randrange

# 0 - Pedra
# 1 - Papel
# 2 - Tesoura

maoPC = randrange(0, 3)
maoUser = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\n'))
if 0 <= maoUser <= 2:
    if maoPC == 0:
        if maoUser == 0:
            print('Empate: Ambos jogaram pedra')
        elif maoUser == 1:
            print('Você ganhou! O PC jogou pedra')
        else:
            print('Você perdeu! O PC jogou pedra')
    elif maoPC == 1:
        if maoUser == 0:
            print('Você perdeu! O PC jogou papel')
        elif maoUser == 1:
            print('Empate: Ambos jogaram papel')
        else:
            print('Você ganhou! O PC jogou papel')
    else:
        if maoUser == 0:
            print('Você ganhou! O PC jogou tesoura')
        elif maoUser == 1:
            print('Você perdeu! O PC jogou tesoura')
        else:
            print('Empate: Ambos jogaram tesoura')
else:
    print("Erro: digite uma opção válida.")