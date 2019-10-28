v = float(input('Valor do produto: '))
meio = int(input('Pagamento:\n1 - À vista\n2 - Parcelado'))

if meio == 1:
    desc = v*0.9
    print('À vista pelo dinheiro/cheque: {}'.format(desc))
    desc = v*0.95
    print('À vista pelo cartão: {}'.format(desc))
elif meio == 2:
    acr = v*1.2
    print('2x no cartão: {}'.format(v))
    print('3x ou mais no cartão: {}'.format(acr))
else:
    print('Erro: Digite uma opção válida [1 ou 2]')