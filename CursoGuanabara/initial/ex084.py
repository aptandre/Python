exo = []
pessoas = []
pesados = []
leves = []
nbts = minp = maxp = 0
while True:
    nome = input('Digite um nome: ')
    peso = int(input('Digite o peso: '))
    if nbts == 0:
        minp = maxp = peso
    else:
        if peso > maxp:
            maxp = peso
        elif peso < minp:
            minp = peso
    #Notes da aula: Dá para colocar o input direto no append
    pessoas.append(nome)
    pessoas.append(peso)
    exo.append(pessoas[:])
    pessoas.clear()
    nbts += 1
    continuar = input('Digite se deseja continuar: ')
    if continuar in 'Nn':
        break
for x in exo:
    if maxp in x:
        pesados.append(x[0])
    elif minp in x:
        leves.append(x[0])
print(f'O número de pessoas cadastradas foi {len(exo)}\nAs pessoas mais pesadas foram {pesados} com {maxp}kg \nAs pessoas mais leves foram {leves} com {minp}kg')
