casa = float(input('Digite o valor, em reais, da casa que você pretende comprar: '))
salario = float(input('Quantos reais você recebe mensalmente? '))
anos = int(input('Em quantos anos você pretende pagar a casa? '))

prestacao = casa/(12 * anos)

if prestacao > salario * 0.3 :
    print('Empréstimo negado. O valor da prestção mensal da casa excedeu 30% do seu salário! ({})'.format(prestacao))
else:
    print('Empréstimo concedido. A prestação mensal da sua casa tem o valor de {}R$.'.format(prestacao))