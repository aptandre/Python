'''from pygame import mixer
mixer.init()
mixer.music.load('Fancy.mp3')
mixer.music.play()
play = input('Agora você escuta? ')
if play == 'PARE':
    mixer.music.stop'''

#Both code works, unfortunately, none are mine :(, MAS A  IMPLEMENTAÇÃO DA LISTA FOI *-*

import pygame
from random import shuffle
lista = ['DNA.mp3', 'Fancy.mp3', 'Havana.mp3', 'Zimzalabim.mp3', 'FIRE.mp3']
shuffle(lista)
pygame.mixer.init()
pygame.mixer.music.load(lista[0])
pygame.mixer.music.play()
play = input('Agora você escuta? ').upper()
if play == 'PARE':
    pygame.mixer.music.stop

#tem outro módulo também, o playsound import playsound 