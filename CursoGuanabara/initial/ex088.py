import random
import time
w = f = 1
jogos = int(input('Digite o número de jogos: '))
hitormiss = []
fireaway = []
while f <= jogos:
    for s in range(0, 6):
        num = random.randint(1, 60)
        if num not in hitormiss:
            hitormiss.append(num)
        else:
            num = random.randint(1, 60)
            hitormiss.append(num)
    fireaway.append(hitormiss[:])
    hitormiss.clear()
    f+=1
print(f'============== SORTEANDO {jogos} JOGOS ==============')
for p in range(0, len(fireaway)):
    print(f'Jogo {w}: {fireaway[p]}')
    w += 1
    time.sleep(0.5)
#Estudar mais sobre o enumerate porque economizaria linha desse W aí!
print('Boa sorte!')