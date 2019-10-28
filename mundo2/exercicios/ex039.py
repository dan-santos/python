ano = int(input('Você nasceu em que ano? '))
idade = 2019 - ano
if idade < 18:
    print('Você ainda não precisa se alisar, faltam {} anos'.format(18-idade))
elif idade > 18:
    print('Você está {} anos atrasado para o alistamento, guerreito.'.format(idade-18))
else:
    print('Você no ano certo para o alistamento militar.')