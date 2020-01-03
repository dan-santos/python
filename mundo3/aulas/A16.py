lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#Tuplas são imutáveis
print(lanche)
print(lanche[-2]) #com número negativos, se começa a contar a partir do último
print(lanche[-3:]) #apesar de ser número negativo, o ":" continua percorrendo o texto da esquerda para a direita

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate (lanche): #Quando se precisa saber a posição do item
    print(f'A {pos+1}a comida é {comida}')

print(sorted(lanche)) #Mostrando por ordem alfabética

a = (2, 5, 4) #Tupla
b = (5, 8, 1, 2)
c = a+b # != b+a
del(a) #deletando a tupla "a"
print(c.count(5)) #count = conta quantas vezes determinado item aparece no obj
print(c.index(5)) #index = aponta em qual posição está o item
print(c.index(5, 2)) # aponta a posição do primeiro número a partir da posição de índice = ao segundo número
# as tuplas alocam tipos diferentes de dados
