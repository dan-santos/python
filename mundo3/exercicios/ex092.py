from datetime import date
reg = {'nome':str(input('Nome: ')),
       'sexo':str(input('Sexo [F/M]: ')),
       'idade':date.today().year - int(input('Ano de nascimento: ')),
       'ctps':int(input('CTPS [sem pontos, traços e espaços]: '))}
if reg['ctps'] != 0:
    reg['anoContratacao'] = int(input('Ano de contratação: '))
    reg['salario'] = float(input('Salário: '))
    if reg['sexo'] in 'Mm':
        pontos = 96
    else:
        prontos = 86
    reg['aposentarEm'] = pontos - reg['idade']+(date.today().year - reg['anoContratacao'])

for k, v in reg.items():
    print(f'{k} = {v}')
