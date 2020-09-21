jogador = dict()
x = 0
jogadorList = []
while True:
    jogador['Nome'] = input("Digite o nome do jogador: ")
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidasList = []
    for partida in range(0, partidas):
        partidasList.append(int(input(f'Digite a quantidade de gols na partida {partida + 1}: ')))
    continuar = input('Deseja continuar? [S/N] ')
    jogador['Gols'] = partidasList[:]
    jogador['Total'] = sum(partidasList)
    jogadorList.append(jogador.copy())
    if continuar in 'nNnaoNOPEnopeNO':
        break
print(f'{"ID":>1} {"NOME":<15} {"GOLS":<15} {"TOTAL":<15}')
for player, valor in enumerate(jogadorList):
    print(f'{player:>1}   ', end='')
    for d in valor.values():
        print(f'{str(d):<15}', end='')
    print()
#A formatação é feita através de listas