def ficha(nome = 'inexistente', gols = 'nenhum'):
    if nome == '' and (gols == '' or gols == '0'):
        nome = 'inexistente'
        gols = 'nenhum'
    return f'O jogador {nome} fez {gols} gol(s).'


print(ficha(str(input('Nome do jogador: ')), input('Gols marcados: ')))