import pygame

pygame.init()
pygame.mixer.load('ex016.mp3')
pygame.mixer.music.play()
pygame.event.wait()