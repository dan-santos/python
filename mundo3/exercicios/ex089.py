reg = list()
while True:
    aluno = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2)/2
    reg.append([aluno, [nota1, nota2], media])
    opt = str(input("Deseja cadastrar outro aluno? [Y/N]"))
    if opt in 'Nn':
        break
for i in reg:
    print(i)