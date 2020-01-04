texto = str(input('Digite um texto entre parênteses: '))
lista = []
for char in texto:
    if char == '(':
        lista.append(char)
    elif char == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(char)
            break

if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')
