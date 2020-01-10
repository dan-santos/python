from mundo3.aulas.uteis import numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')

#os códigos dos pacotes é sempre colocado nos arquivos __init__