nasc = int(input('Ano de nascimento: '))
idade = 2019 - nasc

if idade < 10:
    print('MIRIM')
elif idade < 15:
    print('INFANTIL')
elif idade < 20:
    print('JUNIOR')
elif idade < 21:
    print('SÊNIOR')
else:
    print('MASTER')