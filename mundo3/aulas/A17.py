lanche = ['Pizza', 'X-Tudo', 'Hot Dog', 'Taco']
lanche.append('Esfirra') #insere no final
lanche.insert(0, 'Pastel') #insere no índice informado jogando o valor para o lado

del lanche[2] #exclusões por chave
lanche.pop(3) #sem nenhum valor nos parâmetros, o pop e somente ele, eliminará o pultimo valor

lanche.remove('Pizza') #exclusão por valor

a = [1, 2, 4]
b = a #Estabelcendo uma ligação entre duas listas
# o B não está recebendo os valores de A nesse caso
#prova:
b[1] = 3
print('{} / {} '.format(a, b))

#FORMA CORRETA:
a = [1, 2, 4]
b = a[:] #b recebe todos os valores separadamente da lista a
b[1] = 3
print('{} / {} '.format(a, b))
