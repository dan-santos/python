salario = float(input("Digite seu salário (em reais): "))
if salario > 1250:
    print("Você recebeu um aumento de 10%. Seu salário agoa é de {}R$".format(salario*1.1))
else:
    print("Você recebeu um aumento de 15%. Seu salário agora é de {}R$".format(salario*1.15))
