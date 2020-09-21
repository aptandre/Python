import random
x = 0
jogadas = dict()
for player in range(0,4):
    jogadas[f'Jogador {x + 1}'] = random.randint(1,6)
    x += 1
'''Dava para fazer um dicionário com o rolê já
dictio = { 'jogador1': random.randint(1,6),
            'jogador2': random.randint(1,6) etc.}'''
print('---VALORES SORTEADOS---')
lista = []
for jogador, num in jogadas.items():
    print(f'{jogador} tirou {num}')
    lista.append(jogador)
    lista.append(num)

#parte que eu não fiz
#Uma nova biblioteca deveria ser importada
from operator import itemgetter

ranking = list()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) #se for 1 pega value, se for 0 pega key.
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')