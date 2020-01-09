player = {'nome':str(input('Nome do jogador: '))}
player['jogos'] = int(input(f'Quantas partidas o {player["nome"]} jogou: '))
gols = list()
totalGols = 0
for i in range(player['jogos']):
    gols.append(int(input(f'Gols na {i+1} partida: ')))
    totalGols += gols[i]

player['gols'] = gols[:]
player['totalGols'] = totalGols
player['media'] = totalGols/player['jogos']

print(f'O jogador {player["nome"]} fez um total de {totalGols} gols em {player["jogos"]}'+
      f' partidas,\nresultando numa média de {player["media"]:.2f} gols por partida.')
print(len(gols))
for i in range(len(gols)):
    print(f'Gols na {i+1} partida: {gols[i]}')
