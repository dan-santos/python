aluno = list()
notas = list()
media = 0

while True:
    aluno.append(str(input('Nome: ')))
    for i in range(2):
        notas.append(float(input(f'{i+1}ª Nota: ')))
    media = (notas[0] + notas[1])/2
    aluno.append(notas[:])
    aluno.append(media)

    notas.clear()
    opt = str(input("Deseja cadastrar outro aluno? [Y/N]"))
    if 'n' in opt or 'N' in opt:
        break

print(aluno)