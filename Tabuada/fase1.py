import time
import pygame
print('Bem vindo à pybuada!')
print('Bem na sua primeira fase, você começará com a adição!')
time.sleep(1)
pygame.mixer.init()
pygame.mixer.music.load("Mario.mp3")
pygame.mixer.music.play()

from random import shuffle
n = 1
while True:
    tab = [x for x in range(11)]
    for i in range(10):
        shuffle(tab)
        print(f'{n} + {tab[0]} = ', end='')
        res = int(input())
        while res != n + tab[0]:
            res = int(input('ERROU! Digite novamente: '))
        tab.pop(0)
    n += 1
    if n <= 9:
        print(f'---Agora com o número {n}!---')
    elif n > 9:
        break
            