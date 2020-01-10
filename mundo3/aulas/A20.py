def lin(frase):
    print('-' * 30)
    print('       ' + frase)
    print('-' * 30)

lin('Curso em vídeo')
lin('Aprenda Python')

#Empacotamento:
#Quando não se sabe quantos parâmetros serão passados
def contador(*num):
    tam = len(num)
    print(f'Peguei os valores {num}, totalizando {tam} números.')

contador(1, 2, 5, 4)

def dobra(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1

valores = [2, 5, 6, 9]
dobra(valores)
print(valores)
