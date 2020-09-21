jogador = dict()
x = 0
jogador['Nome'] = input("Digite o nome do jogador: ")
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
partidasList = []
for partida in range(0, partidas):
    partidasList.append(int(input(f'Digite a quantidade de gols na partida {partida + 1}: ')))
jogador['Gols'] = partidasList
jogador['Total'] = sum(partidasList)
print(f'\nO jogador {jogador["Nome"]} jogou {jogador["Total"]} partidas.')
for k in partidasList:
    print(f'Na partida {x + 1}, {jogador["Nome"]} fez {partidasList[x]} gols.')
    x += 1
print(f'Foi um total de {jogador["Total"]} gols.')