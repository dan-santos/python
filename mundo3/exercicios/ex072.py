nomes = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
'Dezenove', 'Vinte')

nr = int(input('Digite um número entre 0 e 20\n'))
while(0 < nr > 20):
    print('Tente novamente.')
    nr = int(input('Digite um número entre 0 e 20\n'))
print(nomes[nr])