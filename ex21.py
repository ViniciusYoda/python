import pygame
pygame.init()
pygame.mixer.music.load('mus.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
input('Agora você escuta?')