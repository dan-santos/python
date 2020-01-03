palavras = (str(input('Insira uma palavra\n')),
            str(input('Insira uma palavra\n')),
            str(input('Insira uma palavra\n')))

for i in palavras:
    print(i.count('a')
          +i.count('e')
          +i.count('i')
          +i.count('o')
          +i.count('u'))
