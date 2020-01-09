aluno = {'nome':str(input('Nome do aluno: ')),
         'media':float(input('Média do aluno: '))}

if aluno['media'] >= 5:
    aluno['situacao'] = 'APROVADO'
else:
    aluno['situacao'] = 'REPROVADO'

print(f'A situação do aluno {aluno["nome"]}, que obteve média'+
      f' igual a {aluno["media"]} é {aluno["situacao"]}.')