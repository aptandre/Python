def jogador(nome='desconhecido', gols=0):
    if nome == '':
        nome = 'desconhecido'
    if gols == '':
        gols = 0
    return print(f'O jogador {nome} fez {gols} gols.')

nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols: ')
jogador(nome, gols)