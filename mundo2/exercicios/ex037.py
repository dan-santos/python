nr = int(input('Digite um número inteiro qualquer: '))
opcao = int(input('Para qual base você quer converter?\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))

if opcao == 1:
    resultado = bin(nr)
    print(resultado)
elif opcao == 2:
    resultado = oct(nr)
    print(resultado)
elif opcao == 3:
    resultado = hex(nr)
    print(resultado)
else:
    print('Erro: digite uma opção válida.')
