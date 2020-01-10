try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError): #Se for erro de valor ou tipo
    print(f'Problema com o tipo de dados que você digitou')
except ZeroDivisionError:
    print('Erro: o denominador nunca pode ser igual a 0')
except KeyboardInterrupt: #quando o user clica enter sem digitar nada
    print('é impossível realizar a operação sem todos os valores solicitados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')