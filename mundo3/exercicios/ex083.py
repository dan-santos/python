texto = str(input('Digite um texto entre parênteses: '))

if '(' in texto:
    if ')' in texto:
        abre = texto.count('(')
        fecha = texto.count(')')
        if abre == fecha:

        else:
            print('Ta errado!')
    else:
        print('Ta errado!')
else:
    print('Ta errado!')

